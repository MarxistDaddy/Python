
def  record_spell(spell_name: str, ingredients: str) -> str:    
    from alchemy.grimoire import validate_ingredients
    validate = validate_ingredients(ingredients)
    if "INVALID" in validate:
        return f"spell rejected: {spell_name} ({validate})"
    else:
        return f"spell recorded: {spell_name} ({validate})"

