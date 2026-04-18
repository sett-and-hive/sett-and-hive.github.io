from pydantic import BaseModel, Field, model_validator


class Blip(BaseModel):
    name: str
    quadrant: str
    ring: str
    is_new: bool = Field(alias="isNew", default=False)
    description: str


class Radar(BaseModel):
    title: str
    quadrants: list[str]
    rings: list[str]
    blips: list[Blip]

    @model_validator(mode="after")
    def validate_blips_match_radar(self) -> Radar:
        quadrants_set = set(self.quadrants)
        rings_set = set(self.rings)

        for i, blip in enumerate(self.blips):
            if blip.quadrant not in quadrants_set:
                msg = (
                    f"Blip {i} ('{blip.name}') has invalid quadrant '{blip.quadrant}'. "
                    f"Must be one of: {self.quadrants}"
                )
                raise ValueError(msg)
            if blip.ring not in rings_set:
                msg = (
                    f"Blip {i} ('{blip.name}') has invalid ring '{blip.ring}'. "
                    f"Must be one of: {self.rings}"
                )
                raise ValueError(msg)
        return self
