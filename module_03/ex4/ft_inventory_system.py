
def display_inventory(player_name):
    inventory = players[player_name]
    print(f"=== {player_name}'s Inventory ===")
    total_value = 0
    total_items = 0
    category = 

    for itam_name, item_value in inventory.items():
        quantity = item_value["quantity"]
        value = item_value["value"]
        typee = item_value["type"]
        rarity = item_value["rarity"]

        total_quantity += quantity
        total_value += (value * quantity)

        


print("=== Player Inventory System ===\n")
players = {
    "alice": {
        "sword": {"type": "weapon", "rarity": "rare", "quantity": 1, "value": 500},
        "potion": {"type": "consumable", "rarity": "common", "quantity": 5, "value": 50},
        "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1, "value": 200},
    },
    "bob": {
        "magic_ring": {"type": "accessory", "rarity": "legendary", "quantity": 1, "value": 800},
    }
}


display_inventory("alice")
display_inventory("bob")






