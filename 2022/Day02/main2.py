f = open('input.txt', 'r')

score = 0

for line in f:
    play = line[:-1].split(' ')
    if play[0] == 'A':  # opponent plays rock
        if play[1] == 'X':  # you need to lose
            score += 3 + 0
        if play[1] == 'Y':  # you need a draw
            score += 1 + 3
        if play[1] == 'Z':  # you need to win
            score += 2 + 6

    if play[0] == 'B':  # opponent plays paper
        if play[1] == 'X':  # you need to lose
            score += 1 + 0
        if play[1] == 'Y':  # you need a draw
            score += 2 + 3
        if play[1] == 'Z':  # you need to win
            score += 3 + 6

    if play[0] == 'C':  # opponent plays scissors
        if play[1] == 'X':  # you need to lose
            score += 2 + 0
        if play[1] == 'Y':  # you need a draw
            score += 3 + 3
        if play[1] == 'Z':  # you need to win
            score += 1 + 6

print(score)
