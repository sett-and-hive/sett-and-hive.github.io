import pytest
from pydantic import ValidationError

from sett_and_hive_radar.models import Radar


def test_valid_radar():
    data = {
        "title": "Test Radar",
        "quadrants": ["q1"],
        "rings": ["r1"],
        "blips": [
            {"name": "b1", "quadrant": "q1", "ring": "r1", "isNew": True, "description": "desc"}
        ],
    }
    radar = Radar(**data)
    assert radar.title == "Test Radar"
    assert len(radar.blips) == 1
    assert radar.blips[0].name == "b1"
    assert radar.blips[0].is_new is True


def test_invalid_quadrant():
    data = {
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
        Radar(**data)


def test_invalid_ring():
    data = {
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
        Radar(**data)
