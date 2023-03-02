from itertools import islice

uppercase = {chr(i): i-38 for i in range(65, 91)}
lowercase = {chr(i): i-96 for i in range(97, 123)}

def split_halfway(string):
    return (string[:int(len(string) / 2)], string[int(len(string) / 2):])

def sameLetter(one, two, three = ''):
    for char in one:
        if char in two:
            if three == '':
                return char
            else:
                if char in three:
                    return char
    return False

def partOne():
    rucksackList = open('./Day 3/input.txt','r')
    total = 0

    for compartments in rucksackList:
        one, two = split_halfway(compartments)
        duplicate = sameLetter(one,two)
        if duplicate.isupper():
            priority = uppercase[duplicate]
        else:
            priority = lowercase[duplicate]
        total += priority

    print(total)

def partTwo():
    total = 0
    with open('./Day 3/input.txt') as file:
        while True:
            next_n_lines = list(islice(file, 3))
            if not next_n_lines:
                break
            one, two, three = next_n_lines
            duplicate = sameLetter(one, two, three)
            if duplicate.isupper():
                priority = uppercase[duplicate]
            else:
                priority = lowercase[duplicate]
            total += priority

    print(total)

print('====== PART 1 ======')
partOne()
print('====== PART 2 ======')
partTwo()