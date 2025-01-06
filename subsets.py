my_list = [1, -1, 2, -2, 3, -3, 4]

subs = []

list1 = my_list
sub1 = []

for i in range(len(my_list) - 1):
    item = list1.pop(0)
    sub1.append(item)
    subs.append(sub1)

    sub1 = []

list1 = my_list
list2 = my_list
sub2 = []
temp = []
for j in range(len(my_list) - 1):
    temp.clear()
    item1 = list1.pop(0)
    temp.append(item1)
    if list1 != None :
        for i in range(len(list1) - 1):
            list2 = list1
            item2 = list2.pop(0)
            sub2 = temp
            sub2.append(item2)
            subs.append(sub2)




# hala chetor az kari k ghablan krdm esstfade knm?
# chtor bedoon oon beram

print(subs)