# Implement Python radar site generation

## Goal

Generate the radar site from Python instead of the existing JavaScript generator.

## Scope

- Render the radar page from templates.
- Copy or package static assets as needed.
- Keep output paths compatible with the current published site.
- Reproduce the current page structure closely enough to avoid breakage.

## Checklist

- [ ] Render HTML from Python templates
- [ ] Produce the expected static assets
- [ ] Preserve existing output paths and links
- [ ] Verify the generated site opens correctly in a browser

## Acceptance

- The Python generator produces a working `tech-radar/` output directory.
- The generated site is usable on GitHub Pages without extra tooling.
