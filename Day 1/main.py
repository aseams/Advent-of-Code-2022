def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
         
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j];
                 
        list1.remove(max1);
        final_list.append(max1)
    return final_list

elfCalories = open('./Day 1/input.txt','r')

totalCalories = 0
elfTotals = []

for line in elfCalories:
    if not line.rstrip('\n'):
        elfTotals.append(totalCalories)
        totalCalories = 0
    else:
        totalCalories = totalCalories + int(line)

print("====== Part 1 ======")
print(max(elfTotals))
print("====== Part 2 ======")
print(sum(Nmaxelements(elfTotals,3)))