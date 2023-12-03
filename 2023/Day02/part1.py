f = open("input.txt", "r")

bag_config = {"red": 12, "green": 13, "blue": 14}

total = 0


def is_game_possible(color, amount, bag_config):
    return bag_config[color] >= amount


for game in f:
    game_id, sets = game.split(": ")
    game_id = game_id[5:]
    sets = sets.split(";")
    is_possible = True
    for set in sets:
        for n, color in map(str.split, set.split(", ")):
            amount = int(n)
            if not is_game_possible(color, amount, bag_config):
                is_possible = False
    if is_possible:
        total += int(game_id)

print(total)
