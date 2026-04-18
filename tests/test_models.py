import json
from typing import Any

import pytest
from pydantic import ValidationError

from sett_and_hive_radar.models import Blip, Radar
from sett_and_hive_radar.paths import project_root


def test_valid_radar():
    data: dict[str, Any] = {
        "title": "Test Radar",
        "quadrants": ["q1"],
        "rings": ["r1"],
        "blips": [
            {"name": "b1", "quadrant": "q1", "ring": "r1", "isNew": True, "description": "desc"}
        ],
    }
    radar = Radar.model_validate(data)
    assert radar.title == "Test Radar"
    assert len(radar.blips) == 1
    assert radar.blips[0].name == "b1"
    assert radar.blips[0].is_new is True


def test_blip_default_is_new():
    data: dict[str, Any] = {"name": "b1", "quadrant": "q1", "ring": "r1", "description": "desc"}
    blip = Blip.model_validate(data)
    assert blip.is_new is False


def test_blip_rejects_unknown_fields():
    data: dict[str, Any] = {
        "name": "b1",
        "quadrant": "q1",
        "ring": "r1",
        "is_new": True,
        "description": "desc",
    }
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        Blip.model_validate(data)


def test_invalid_quadrant():
    data: dict[str, Any] = {
        "title": "Test Radar",
        "quadrants": ["q1"],
        "rings": ["r1"],
        "blips": [
            {
                "name": "b1",
                "quadrant": "invalid-q",
                "ring": "r1",
                "isNew": True,
                "description": "desc",
            }
        ],
    }
    with pytest.raises(ValidationError, match="invalid quadrant 'invalid-q'"):
        Radar.model_validate(data)


def test_invalid_ring():
    data: dict[str, Any] = {
        "title": "Test Radar",
        "quadrants": ["q1"],
        "rings": ["r1"],
        "blips": [
            {
                "name": "b1",
                "quadrant": "q1",
                "ring": "invalid-r",
                "isNew": True,
                "description": "desc",
            }
        ],
    }
    with pytest.raises(ValidationError, match="invalid ring 'invalid-r'"):
        Radar.model_validate(data)


def test_radar_rejects_unknown_fields():
    data: dict[str, Any] = {
        "title": "Test Radar",
        "quadrants": ["q1"],
        "rings": ["r1"],
        "blips": [],
        "unexpected": "value",
    }
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        Radar.model_validate(data)


def test_real_radar_json():
    json_path = project_root() / "tech-radar.json"
    with json_path.open() as f:
        data = json.load(f)

    # Should not raise any validation error
    radar = Radar.model_validate(data)
    assert radar.title == "Sett-and-Hive Radar"
    assert len(radar.blips) > 0
