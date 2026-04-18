#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def run_command(cmd, check=True):
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def get_changed_python_files(base_branch="origin/main"):
    """Get list of changed .py files in src/ compared to base_branch."""
    try:
        result = subprocess.run(
            ["git", "diff", base_branch, "--name-only", "--", "src/**/*.py"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: Could not get diff from {base_branch}")
        if e.stderr:
            print(e.stderr)
        raise
    else:
        return [f for f in result.stdout.splitlines() if f.endswith(".py")]


def file_to_module(file_path):
    """Convert a file path to a python module path."""
    p = Path(file_path)
    parts = p.parts[1:] if p.parts[0] == "src" else p.parts

    module_parts = list(parts[:-1])
    stem = p.stem
    if stem != "__init__":
        module_parts.append(stem)

    return ".".join(module_parts)


def file_to_module_path(file_path):
    """Convert a changed file path to a valid cosmic-ray module-path target."""
    path = Path(file_path)
    if path.name == "__init__.py":
        return str(path.parent)
    return str(path)


def main():
    parser = argparse.ArgumentParser(description="Run scoped mutation testing")
    parser.add_argument(
        "--base",
        default="origin/main",
        help="Base branch for diff (default: origin/main)",
    )
    args = parser.parse_args()

    changed_files = get_changed_python_files(args.base)
    if not changed_files:
        print("No changed Python files found in src/.")
        sys.exit(0)

    modules = [file_to_module(f) for f in changed_files]
    module_paths = [file_to_module_path(f) for f in changed_files]
    print(f"Changed modules: {', '.join(modules)}")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        config_path = tmp_path / "cosmic-ray.toml"
        session_path = tmp_path / "session.sqlite"

        base_config = """
[cosmic-ray]
module-path = "src/sett_and_hive_radar"
python-version = "3.14"
test-command = "pytest"
timeout = 10.0

[cosmic-ray.distributor]
name = "local"
"""
        for module, module_path in zip(modules, module_paths, strict=True):
            print(f"\n--- Testing module: {module} ---")

            scoped_config = base_config.replace(
                'module-path = "src/sett_and_hive_radar"',
                f'module-path = "{module_path}"',
            )
            config_path.write_text(scoped_config)

            try:
                run_command(
                    [
                        "uv",
                        "run",
                        "cosmic-ray",
                        "init",
                        "--force",
                        str(config_path),
                        str(session_path),
                    ]
                )
                run_command(
                    ["uv", "run", "cosmic-ray", "exec", str(config_path), str(session_path)]
                )

                dump_result = run_command(["uv", "run", "cosmic-ray", "dump", str(session_path)])

                survivors = 0
                for line in dump_result.stdout.splitlines():
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if (
                        isinstance(data, list)
                        and len(data) > 1
                        and data[1].get("test_outcome") == "survived"
                    ):
                        survivors += 1
                        print(f"MUTANT SURVIVED: {data[1].get('diff')}")

                if survivors > 0:
                    print(f"FAILURE: {survivors} mutants survived in {module}")
                    sys.exit(1)
                else:
                    print(f"SUCCESS: All mutants killed in {module}")

            except subprocess.CalledProcessError as e:
                print(f"Error during cosmic-ray execution for {module}:")
                print(e.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
