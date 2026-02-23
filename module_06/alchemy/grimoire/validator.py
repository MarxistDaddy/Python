#from .spellbook import record_spell

def validate_ingredients(ingredients: str) -> str:
    data = ingredients.split()
    for s in data:
        if s.lower() not in ["fire", "water", "air", "earth"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

