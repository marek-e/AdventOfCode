f = open("input.txt", "r")

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_digits(line):
    digits = []
    for word, digit in word_to_digit.items():
        if word in line:
            index = line.find(word)
            digits.append((word, index))
    if digits:
        digits.sort(key=lambda x: x[1])
        word = digits[0][0]
        line = line.replace(word, word_to_digit.get(word, None))
        word = digits[-1][0]
        line = line.replace(word, word_to_digit.get(word, None))

    return [char for char in line if char.isdigit()]


res1 = []

sum = 0
for line in f:
    digits = extract_digits(line)
    res1.append(int(digits[0] + digits[-1]))
    sum += int(digits[0] + digits[-1])

print(sum)
