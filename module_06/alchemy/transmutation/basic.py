from alchemy.elements import create_fire, create_earth

create_fire()

def lead_to_gold():
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem():
    return f"Stone transmuted to gem using {create_earth}"
