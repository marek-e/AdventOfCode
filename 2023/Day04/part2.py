from collections import defaultdict

f = open("input.txt", "r")

scratches = defaultdict(lambda: 1)

for line in f:
    game_id, numbers = line.split(": ")
    winning, my_numbers = numbers.split(" | ")
    winning = winning.split(" ")
    winning_nb = []
    for i in winning:
        if i.isdigit():
            winning_nb.append(int(i))

    my_numbers = my_numbers.strip().split(" ")
    game_id = int(game_id[5:])

    points = 0
    for nb in filter(lambda x: x.isdigit(), my_numbers):
        if int(nb) in winning_nb:
            points += 1

    for i in range(game_id + 1, game_id + points + 1):
        scratches[i] += scratches[game_id]
    scratches[game_id]  # for non winning games to be added to the total

print(sum(scratches.values()))
