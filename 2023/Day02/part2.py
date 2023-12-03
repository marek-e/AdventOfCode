f = open("input.txt", "r")

total = 0

for game in f:
    game_id, sets = game.split(": ")
    game_id = game_id[5:]
    sets = sets.split(";")
    min_red = min_green = min_blue = 0
    for set in sets:
        red = green = blue = 0
        for n, color in map(str.split, set.split(", ")):
            amount = int(n)
            if color == "red":
                red += amount
            if color == "green":
                green += amount
            if color == "blue":
                blue += amount
        min_red = max(red, min_red)
        min_green = max(green, min_green)
        min_blue = max(blue, min_blue)
    total += min_red * min_green * min_blue

print(total)
