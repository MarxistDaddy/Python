from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


#we start by creating a class that will validate our data!
#this class inherit from basemodel and it will create the contract that we need to follow! 
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True #feault value 
    notes: Optional[str] = Field(default=None, max_length=200) #default is none!


def main():
    print("Space Station Data Validation")
    print("========================================")
    
    #
    station = SpaceStation(
        station_id="ISS001", #6 length
        name="International Space Station", #  1 <  length < 50
        crew_size=6, #  1 <= n <= 20
        power_level=85.5, #same
        oxygen_level=92.3, 
        last_maintenance="2026-02-20T10:30:00" #it will be translated directly to time!
    )


    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    print(f"Status: {'Operational' if station.is_operational else 'Offline'}") 
    
    print("========================================")
    try:
        wrong_station = SpaceStation(
            station_id="BAD001",
            name="Broken Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance="2026-02-20T10:30:00"
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

if __name__ == "__main__":
    main()
