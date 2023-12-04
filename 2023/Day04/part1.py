f = open("input.txt", "r")

total = 0
for line in f:
    points = 0
    line = line.split(": ")[1]
    winning, my_numbers = line.split(" | ")
    winning = winning.split(" ")
    winning_nb = []
    for i in winning:
        if i.isdigit():
            winning_nb.append(int(i))

    my_numbers = my_numbers.strip().split(" ")

    for nb in filter(lambda x: x.isdigit(), my_numbers):
        if int(nb) in winning_nb:
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points

print(total)
