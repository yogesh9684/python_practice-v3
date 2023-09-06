#Approch 1

List1 = [11,44,999,66,22,500,777,200,1000]
List1.sort()
print(List1)
print(List1[-2])

# Approch 2
# Remove Duplicate using Set
# Convert SET in to List
# Sort the List
# Print the second Largest Number

List1 = [11,66,44,66,999,66,22,500,777,11,200,1000]
# Remove Duplicate using Set
MySet = set(List1)
print(MySet)
# Convert SET in to List
mylist = list(MySet)
print(mylist)
# Sort the List
mylist.sort()
print(mylist)
# Print the Second Largest Number
print(mylist[-2])

#Approch 3

List1 = [11,66,44,66,999,66,22,500,777,11,200,1000]
myset = set(List1)
myset.remove(max(myset))
print(myset)
MYLIST = list(myset)
print(MYLIST)
MYLIST.sort()
print(MYLIST)
print(MYLIST[-1])