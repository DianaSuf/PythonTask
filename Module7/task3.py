# Игроки
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = [(player[0], player[1]) + scores for player, scores in players.items()]

print(result)