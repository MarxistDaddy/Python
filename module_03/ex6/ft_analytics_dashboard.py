players = {
    'alice': {"score": 2300, "status": "active"},
    'bob': {"score": 1800, "status": "active"},
    'charlie': {"score": 2150, "status": "active"},
    'diana': {"score": 2300, "status": "offline"}
}

players_achievements = {
    'alice': ('first_kill', 'level_10', 'boss_slayer', 'treasure_hunter', 'speed_runner'),
    'bob': ('first_kill', 'level_5', 'speed_runner'),
    'charlie': ('first_kill', 'level_10', 'boss_slayer', 'treasure_hunter', 'speed_runner', 'collector', 'strategist'),
    'diana': ('level_10', 'boss_slayer', 'speed_runner')
}

players_regions = {
    'alice': 'north',
    'bob': 'east',
    'charlie': 'central',
    'diana': 'north'
}


def list_cmp(players):
    print("=== List Comprehension ===")
    name = players.items()
    players = [player for player, score in name if score["score"] > 2000]
    print("High scores (>2000): ", players)
    doubled = [score["score"]*2 for player, score in name if score["score"] > 2000]
    print("Scores doubled: ", doubled)
    active = [player for player, status in name if status["status"] == "active"]
    print("Active players: ", active)


def dict_cmp(players):
    print("=== Dict Comprehension ===")
    player = players.items()	#(alice: {})
    dict_player = {}
    for name, stats in player:
        if name not in dict_player:
           dict_player[name] = stats["score"]

    print("Player scores: ", dict_player)
    dict_score = {
        "high": sum(1 for p in players.values() if p["score"] > 2000),
        "meduim": sum(1 for p in players.values() if p["score"] == 2000),
        "low": sum(1 for p in players.values() if p["score"] < 2000)
        }
    print("Score categories: ", dict_score)

    
    achievement = {}
    for n, a in players_achievements.items():
        if n not in achievement:
           achievement[n] = len(a)

    print("Achievement counts: ", achievement)


def set_cmp(players, players_achievements):
    print("=== Set Comprehension ===")
    
    unique_players = {player for player in players}

    unique_achievements = {
        ach
        for achs in players_achievements.values()
        for ach in achs
    }

    active_regions = {
        players_regions[player]
        for player, data in players.items()
        if data["status"] == "active"
    }

    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)
 
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    list_cmp(players)
    print("")
    dict_cmp(players)
    print("")
    set_cmp(players, players_achievements)

