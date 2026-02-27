from enum import Enum
from pydantic import BaseModel, Field, model_validate
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=3, max_length=50)
    rank: Rank = Rank
    age: int = Field(qe=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(qe=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_data = datetime
    duration_days: int = Field(qe=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(eq-0.1, le=10000.0)

    @model_validator(mode="after")
    def validate_rules(self):
        if not slef.mission_id.starswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        #understans this code!
        has_leader = any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")

        if self


if __name__ == "__main__":
    main()

