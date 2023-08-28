# #Approch 1
# List1 = [1,2,4,5,6,7,8]
# print(List1)
# Sample_List = List1.copy()
# print(Sample_List)
#
# print("=============================================")
#
# #Approch 2
# List1 = [1,2,4,5,6,7,8]
# print(List1)
# Sample_List_1 = List1[:]
# print(Sample_List_1)
#
# print("=============================================")
#
# #Approch 3
#
# List1 = [1,2,4,5,6,7,8]
# print(List1)
# Sample_List_2 = list(List1)
# print(Sample_List_2)

print("=============================================")

List1 = [1,2,4,5,6,7,8]
print(List1)
List2 = []
for i in List1:
    if i not in List2:
        List2.append(i)
print(List2)