import string
f = open('input.txt', 'r')

sum = 0

for line in f:
    n = len(line)
    compartment1 = line[:n//2]
    compartment2 = line[n//2:]
    common_char = ''.join(set(compartment1).intersection(compartment2))
    sum += list(string.ascii_letters).index(common_char) + 1

print(sum)
