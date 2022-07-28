# 4 liner wip
# list = [3,1,5,6,7,3,5,7,4]
# for i in range(0,len(list)):
#     if list.count(list[i]) == 2:
#         print(list.pop(i))
##########################################


list = [5,1,4,6,7,3,5,7,3]
duplicate = []
for x in list:
    if list.count(x) >= 2:
        if x not in duplicate:
            duplicate.append(x)
print(duplicate)