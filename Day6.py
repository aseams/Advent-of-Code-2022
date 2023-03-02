file = open('./Day 6/input.txt', 'r')
data = file.read()

for i in range(4, len(data)):
    s = set(data[(i-4):i])
    if len(s) == 4:
        print("Answer to part 1: ", i)
        break

for i in range(14, len(data)):
    s = set(data[(i-14):i])
    if len(s) == 14:
        print("Answer to part 2: ", i)
        break