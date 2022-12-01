f = open("./input.txt", "r")
cal_by_elf = []  # list of calories carried by each elf
cur_sum = 0
for line in f:
    if (line == '\n'):
        cal_by_elf.append(cur_sum)
        cur_sum = 0
    else:
        cur_sum += int(line)

print(max(cal_by_elf))
cal_by_elf.sort()
print(cal_by_elf[-1]+cal_by_elf[-2]+cal_by_elf[-3])
