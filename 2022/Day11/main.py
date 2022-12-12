#!/usr/bin/env python3
f = open('input.txt', 'r')


class Monkey:

    def __init__(self, starting_items, op, div):
        self.items = starting_items
        self.op = op
        self.div = div
        self.nb_inspection = 0

    def append(self, item):
        self.items.append(item)

    def add_throw_monkey(self, on_true, on_false):
        self.true_throw = on_true
        self.false_throw = on_false

    def inspect(self, is_divided):
        for item in self.items:
            self.nb_inspection += 1
            i = self.op(item)
            if is_divided:
                i = i//3
            i = i % (2*7*13*19*11*5*3*17)
            if i % self.div == 0:
                self.true_throw.append(i)
            else:
                self.false_throw.append(i)
        self.items = []


m0 = Monkey([62, 92, 50, 63, 62, 93, 73, 50], lambda x: x * 7, 2)
m1 = Monkey([51, 97, 74, 84, 99], lambda x: x+3, 7)
m2 = Monkey([98, 86, 62, 76, 51, 81, 95], lambda x: x+4, 13)
m3 = Monkey([53, 95, 50, 85, 83, 72], lambda x: x+5, 19)
m4 = Monkey([59, 60, 63, 71], lambda x: x*5, 11)
m5 = Monkey([92, 65], lambda x: x*x, 5)
m6 = Monkey([78], lambda x: x+8, 3)
m7 = Monkey([84, 93, 54], lambda x: x+1, 17)

m0.add_throw_monkey(m7, m1)
m1.add_throw_monkey(m2, m4)
m2.add_throw_monkey(m5, m4)
m3.add_throw_monkey(m6, m0)
m4.add_throw_monkey(m5, m3)
m5.add_throw_monkey(m6, m3)
m6.add_throw_monkey(m0, m7)
m7.add_throw_monkey(m2, m1)

# for _ in range(20):
#     m0.inspect(True)
#     m1.inspect(True)
#     m2.inspect(True)
#     m3.inspect(True)
#     m4.inspect(True)
#     m5.inspect(True)
#     m6.inspect(True)
#     m7.inspect(True)

# print("Monkey 0 ---> ", m0.nb_inspection)
# print("Monkey 1 ---> ", m1.nb_inspection)
# print("Monkey 2 ---> ", m2.nb_inspection)
# print("Monkey 3 ---> ", m3.nb_inspection)
# print("Monkey 4 ---> ", m4.nb_inspection)
# print("Monkey 5 ---> ", m5.nb_inspection)
# print("Monkey 6 ---> ", m6.nb_inspection)
# print("Monkey 7 ---> ", m7.nb_inspection)


# l = [m0.nb_inspection, m1.nb_inspection, m2.nb_inspection, m3.nb_inspection,
#      m4.nb_inspection, m5.nb_inspection, m6.nb_inspection, m7.nb_inspection]
# l.sort()
# print("Monkey business :", l[-1]*l[-2])


for k in range(10000):
    if not k % 10:
        print(k)
    m0.inspect(False)
    m1.inspect(False)
    m2.inspect(False)
    m3.inspect(False)
    m4.inspect(False)
    m5.inspect(False)
    m6.inspect(False)
    m7.inspect(False)

print("Monkey 0 ---> ", m0.nb_inspection)
print("Monkey 1 ---> ", m1.nb_inspection)
print("Monkey 2 ---> ", m2.nb_inspection)
print("Monkey 3 ---> ", m3.nb_inspection)
print("Monkey 4 ---> ", m4.nb_inspection)
print("Monkey 5 ---> ", m5.nb_inspection)
print("Monkey 6 ---> ", m6.nb_inspection)
print("Monkey 7 ---> ", m7.nb_inspection)


l = [m0.nb_inspection, m1.nb_inspection, m2.nb_inspection, m3.nb_inspection,
     m4.nb_inspection, m5.nb_inspection, m6.nb_inspection, m7.nb_inspection]
l.sort()
print("Monkey business :", l[-1]*l[-2])
