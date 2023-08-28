
#Approch 1
List = [1,3,2,6,3,5,6]

List[0] = 6
List[-1]= 1

print(List)

#Approch 2
List = [1,3,2,6,3,5,6]
size = len(List)

temp = List[0]
List[0] = List[size-1]
List[size-1]= temp

print(List)

#Approch 3

List = [1,3,2,6,3,5,6]
List[0] , List[-1] = List[-1] , List[0]
print(List)

#Approch 4
List = [1,3,2,6,3,5,6]

First = List.pop(0)
Last = List.pop(-1)

List.insert(0,Last)
List.append(First)
print(List)