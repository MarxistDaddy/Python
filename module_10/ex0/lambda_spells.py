artifacts = [
    {
        'name': 'Ice Wand',
        'power': 92,
        'type': 'armor'
    },
    {
        'name': 'Ice Wand',
        'power': 95,
        'type': 'relic'
    },
    {
        'name': 'Wind Cloak',
        'power': 70,
        'type': 'armor'
    },
    {
        'name': 'Light Prism',
        'power': 71,
        'type': 'weapon'
    }
]

mages = [
    {
        'name': 'River',
        'power': 97,
        'element': 'earth'
    },
    {
        'name': 'Nova',
        'power': 63,
        'element': 'lightning'
    },
    {
        'name': 'Luna',
        'power': 97,
        'element': 'ice'
    },
    {
        'name': 'Riley',
        'power': 55,
        'element': 'wind'
    },
    {
        'name': 'Rowan',
        'power': 59,
        'element': 'wind'
    }
]

spells = [
        'fireball',
        'blizzard',
        'heal',
        'lightning'
    ]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
        }


def main():
    print("Testing artifact sorter...")
    lst = artifact_sorter(artifacts)
    print(f"first item {lst[0]['name']} ({lst[0]['power']} power)"
          f" last item {lst[-1]['name']} ({lst[-1]['power']} power)")
    print("\nTesting spell transformer...")
    print(mage_stats(mages))
    lst = spell_transformer(spells)
    for v in lst:
        print(v, end=" ")
    print("\n\nTesting mage stats...")
    print(mage_stats(mages))
    print("\nTesting power filter...")
    print(power_filter(mages, 70))


if __name__ == "__main__":
    main()
