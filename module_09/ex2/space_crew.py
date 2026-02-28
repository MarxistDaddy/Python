from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime #what does it do??
from typing import List


#we created our enum | whats the relationship between enum and basemodel and model_validator?
class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


#then we createed our crew, using basenodel 
class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=3, max_length=50)
    rank: Rank #takes from rank enum! why we didnt sign a value here!,
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


#base model for space mission, and model_validator validate fields!
class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12) #take a list of crewmembers!
    mission_status: str = "planned"
    budget_millions: float = Field(ge=0.1, le=10000.0)

    #whats mode?
    #why do we return self?
    @model_validator(mode="after")
    def validate_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        #validate space and enum ranks!
        #understans this code!
        has_leader = any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")

        #validate space and member basemodesl
        if self.duration_days > 365:
            experienced = [
                member for member in self.crew
                if member.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError("Long missions require 50% experienced crew")
        
        #validate space and member basemodesl
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


#spacemission: list of crewmember > list of rank enum!
def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days="900",
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank="commander",
                    age=45,
                    specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="C02",
                    name="C02",
                    rank="lieutenant",
                    age=34,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="C03",
                    name="Alice Johnson",
                    rank="officer",
                    age=29,
                    specialization="Engineering",
                    years_experience=5,
                )
            ]
        )
        print("Valid mission createed:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days}")
        print(f"Budget: {mission.budget_millions}")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for c in mission.crew:
            print(f" - {c.name} ({c.rank}) - {c.specialization}")
    except Exception as e:
        print(e)
 
    print("=========================================")
    
    try:
        bad = SpaceMission(
            mission_id="f1",
            mission_name="Bad Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=100,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="X12",
                    name="who knows",
                    rank="officer",
                    age=19,
                    specialization="loser",
                    years_experience=6,
                )
            ]
        )
    except Exception as e:
        for err in e.errors():
            print(err["loc"])
            print(err["msg"])




if __name__ == "__main__":
    main()
