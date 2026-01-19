players = {
    "alice": {
        "sword": {
            "type": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500,
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50,
        },
        "shield": {
            "type": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200,
        },
    },
    "bob": {
        "magic_ring": {
            "type": "accessory",
            "rarity": "legendary",
            "quantity": 1,
            "value": 600,
        },
    },
}


def display_inventory(player_name):
    inventory = players[player_name]
    print(f"=== {player_name}'s Inventory ===")
    total_value = 0
    total_items = 0
    category = {}

    for item_name, item_value in inventory.items():
        quantity = item_value["quantity"]
        value = item_value["value"]
        typee = item_value["type"]
        rarity = item_value["rarity"]
        total_items += quantity
        total_value += (value * quantity)

        if typee in category:
            category[typee] += quantity
        else:
            category[typee] = quantity
        print(f"{item_name} ({typee}, {rarity}): "
              f"x{quantity} @ {value} gold each = {value} gold")
    print("")
    print(f"Inventory value: {total_value} gold")
    print(f"Item count {total_items} items")
    first = True
    for k, v in category.items():
        if not first:
            print(", ", end="")
        print(f"{k}({v})", end="")
        first = False
    print("")


def transfer_item(from_player, to_player, item_name, quantity):
    print(f"=== Transaction:"
          f"{from_player} gives {to_player} {quantity} {item_name} ===")
    from_inv = players[from_player]
    to_inv = players[to_player]

    if item_name not in from_inv:
        print(f"Transaction failed, {from_player} does not have item\n")
        return
    if from_inv["potion"]["quantity"] < quantity:
        print("Transaction failed, Not enough potions avaialable!\n")
        return
    from_inv["potion"]["quantity"] -= quantity

    if item_name in to_inv:
        to_inv["potion"]["quantity"] += quantity
    else:
        to_inv[item_name] = {
            "type": "consumable",
            "rarity": "common",
            "quantity": quantity,
            "value": 50
            }

    print("Transaction successful!\n")


def check_update(player1, player2):
    print("=== Updated Inventories ===")
    p1 = players[player1]
    p2 = players[player2]

    p1_item = p1["potion"]["quantity"]
    p2_item = p2["potion"]["quantity"]

    print(f"{player1} potions: {p1_item}")
    print(f"{player2} potions: {p2_item}")
    print("")


def valuable_player(players):
    max_value = 0
    best_player = None

    for player, inv in players.items():
        total = 0
        for item in inv.values():
            total += (item["value"] * item["quantity"])

        if total > max_value:
            max_value = total
            best_player = player

    print(f"Most valuable player: {best_player} ({max_value}) gold")


def most_items(players):
    most_player = 0
    most_items = 0

    for player, inv in players.items():
        total = 0
        for item in inv.values():
            total += item["quantity"]
        if total > most_items:
            most_player = player
            most_items = total
    print(f"Most items: {most_player} ({most_items} items)")


def rarest_items(players):
    rare_items = []
    for player, inventory in players.items():
        for item_name, item_info in inventory.items():
            rare = item_info.get("rarity")
            if rare == "rare" or rare == "legendary":
                rare_items += [item_name]

    print("Rarest items: ", end="")
    print(*rare_items, sep=", ")


def inv_stat(players):
    print("=== Inventory Analytics ===")
    valuable_player(players)
    most_items(players)
    rarest_items(players)


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    display_inventory("alice")
    print("")
    transfer_item("alice", "bob", "potion", 2)
    check_update("alice", "bob")
    inv_stat(players)
