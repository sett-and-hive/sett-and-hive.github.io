# Validate tech-radar.json with typed models

## Goal

Make the radar content schema explicit and fail fast on invalid data.

## Scope

- Model the radar structure in Python.
- Validate title, quadrants, rings, and blips.
- Check allowed ring and quadrant values.
- Validate required fields and types.

## Checklist

- [ ] Define typed models for radar data
- [ ] Add schema validation for required fields
- [ ] Validate allowed quadrant and ring values
- [ ] Add clear error messages for invalid content

## Acceptance

- Invalid `tech-radar.json` fails during the build with useful validation errors.
- Valid data loads into typed Python objects.
