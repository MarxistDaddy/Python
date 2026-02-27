from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from typing import Optional
from datetime import datetime


#how does it work??
class ContactType(str, Enum):
     radio = "radio"
     visual = "visual"
     physical = "physical"
     telepathic = "telepathic"


#basemodel, we are just gonna validate fields here!
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime #is it default
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType #whas that?? | enum!
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500) #whats none?
    is_verified: bool = False

    #this model validator, but here we are gonna validate the values of the fields
    @model_validator(mode="after") #whats mode, if it doesnt exit, it will run error missing why?
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self #why do we return self?


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-02-20T15:00:00",
            location = "Area 51, Nevada",
            contact_type=ContactType("radio"),
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    print("Valid contant report:")
    print(f"ID: {valid.contact_id}")
    print(f"type: {valid.contact_type}")
    print(f"Location: {valid.location}")
    print(f"Signal: {valid.signal_strength}")
    print(f"Duration: {valid.duration_minutes}")
    print(f"Witnesse: {valid.witness_count}")
    print(f"Message: {valid.message_received}")
    print("======================================")
    try:
        invalid = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-02-20T15:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType("telepathic"),
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
