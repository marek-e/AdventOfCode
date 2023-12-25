f = open("input.txt", "r").read().split("\n")

hands = [n.split()[0] for n in f]
bids = [n.split()[1] for n in f]


def get_score(hand):
    if vals[-1] == "J":
        counts.append([(str(hand).count(a), a) for a in vals[:-1]])
        ind = 0
        counts[-1].append((0, "J"))

        ind = counts[-1].index(max(counts[-1]))
        for card in hand:
            if card == "J":
                counts[-1][ind] = (counts[-1][ind][0] + 1, counts[-1][ind][1])
    else:
        counts.append([(str(hand).count(a), a) for a in vals])

    pairs, triples, quad, penta = 0, 0, 0, 0
    for c in counts[-1]:
        if c[0] == 2:
            pairs += 1
        if c[0] == 3:
            triples += 1
        if c[0] == 4:
            quad += 1
        if c[0] == 5:
            penta += 1

    if pairs + triples + quad + penta == 0:
        return 0
    if pairs == 1:
        if triples == 1:
            return 4
        else:
            return 1
    if pairs == 2:
        return 2
    if triples == 1:
        if pairs == 1:
            return 4
        else:
            return 3
    if quad == 1:
        return 5
    if penta == 1:
        return 6


vals = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
counts = []
scores = []
for i, hand in enumerate(hands):
    scores.append((hand, bids[i], get_score(hand), counts[i]))

scores.sort(key=lambda x: [x[-1][i][0] for i in range(13)])
scores.sort(key=lambda x: vals.index(x[0][4]), reverse=True)
scores.sort(key=lambda x: vals.index(x[0][3]), reverse=True)
scores.sort(key=lambda x: vals.index(x[0][2]), reverse=True)
scores.sort(key=lambda x: vals.index(x[0][1]), reverse=True)
scores.sort(key=lambda x: vals.index(x[0][0]), reverse=True)
scores.sort(key=lambda x: x[-2])

somme = sum([int(elem[1]) * (scores.index(elem) + 1) for elem in scores])

print(somme)
