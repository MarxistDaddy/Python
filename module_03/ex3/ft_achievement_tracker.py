print("=== Achievement Tracker System ===")

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

print(f"Player alice achievments: {alice}")
print(f"Player bob achievments: {bob}")
print(f"Player charlie achievments: {charlie}")

print("\n=== Achievement Analytics ===")

unique = alice | bob | charlie
print(f"All unique achievements: {unique}")
print("Total unique achievements:", len(unique))

common = alice & bob & charlie
print(f"\ncommon to all players: '{common}'")


def get_rare(alice, bob, charlie) -> list:
    return ((alice - bob - charlie) | (bob - charlie - alice) | (charlie - alice - bob))

def missing_p(rare, alice, bob, charlie):
    players = [alice, bob, charlie]
    count = len([p for p in players if not p & rare])
    return count

rare = get_rare(alice, bob, charlie)
missing_player = missing_p(rare, alice, bob, charlie)

print(f"Rare achievement: ({missing_player}): {rare}")

print("\nAlice vs Bob common:", alice & bob)
print("Alice unique:", alice - bob)
print("Bob unique:", bob - alice)
