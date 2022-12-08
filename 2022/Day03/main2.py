import string
num_lines = sum(1 for line in open('input.txt'))
f = open('input.txt', 'r')

sum = 0

for i in range(num_lines//3):
    bag1 = f.readline()
    bag2 = f.readline()
    bag3 = f.readline()
    common_char = ''.join(set(bag1.rstrip()).intersection(
        bag2.rstrip()).intersection(bag3.rstrip()))
    sum += list(string.ascii_letters).index(common_char) + 1

print(sum)
