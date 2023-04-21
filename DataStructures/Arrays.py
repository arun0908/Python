"""Practice code for Arrays/Lists in Python"""
# 1. Expenses
exp_list = [2200, 2350, 2600, 2130, 2190]
print("Amount spent in February in excess to amount spent in January: ",
      exp_list[1]-exp_list[0])
print("Total expense in the first quarter: ",
      exp_list[0]+exp_list[1]+exp_list[2])
for i in exp_list:
    if i == 2000:
        print("You spent exactly 2000 in one of the months")
        break
# Alternate solution to above for loop
print("Did i spend 2000 in any month?: ", 2000 in exp_list)
exp_list.append(1980)
exp_list[3] = exp_list[3] - 200
print("Expense list after updating: ", exp_list)

# 2. Movie hero List
hero_list = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print("Length of the list: ", len(hero_list))
hero_list.append('black panther')
print("Updated list: ", hero_list)
hero_list.remove('black panther')
hero_list.insert(3, 'black panther')
print("Updated list: ", hero_list)
hero_list[1:3] = ['doctor strange']
print("Updated list: ", hero_list)
hero_list.sort()
print("Updated list: ", hero_list)

# 3. Odd number in a list
max_num = int(input("Enter the max number till which you want a list of: "))
odd_list = []
for i in range(1, max_num+1):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)
