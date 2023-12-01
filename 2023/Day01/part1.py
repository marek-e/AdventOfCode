f = open("input.txt", "r")

sum = 0

for line in f:
    digits = [char for char in line if char.isdigit()]
    if digits:
        sum += int(digits[0] + digits[-1])

print(sum)
