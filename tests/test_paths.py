from sett_and_hive_radar import project_root


def test_project_root_points_to_repository_root() -> None:
    root = project_root()

    assert (root / "tech-radar.json").is_file()
    assert (root / "issues").is_dir()
