from pydantic import BaseModel, Field, field_validator

class UserInput(BaseModel):
    user_id: str = Field(min_length=1, max_length=80)
    name: str = Field(min_length=1, max_length=120)
    age: int = Field(ge=13, le=100)
    weight: str = Field(min_length=1, max_length=30)
    goal: str = Field(min_length=2, max_length=80)
    intensity: str

    @field_validator("intensity")
    @classmethod
    def valid_intensity(cls, v):
        v = v.lower().strip()
        if v not in {"low", "medium", "high"}:
            raise ValueError("Intensity must be low, medium, or high")
        return v

class FeedbackRequest(BaseModel):
    user_id: str = Field(min_length=1, max_length=80)
    feedback: str = Field(min_length=3, max_length=2000)
