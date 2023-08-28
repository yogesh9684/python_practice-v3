
#Approch 1

Array_Elements= [ 1,4,3,2,6,9,4,512,43]
Max_Element = Array_Elements[0]
n = len(Array_Elements)

for i in range(1, n):
    if Array_Elements[i] > Max_Element:
        Max_Element = Array_Elements[i]
print("Max Element from Array is", Max_Element)

#Approch 2

Array_Elements= [ 1,4,3,2,6,9,4,512,43]
print(max(Array_Elements))

#Printing the Minimum Value From Array Element

Array_Elements= [1,4,3,2,6,9,4,512,43]
Min_Element = Array_Elements[0]
n = len(Array_Elements)

for i in range(1 , n):
    if Array_Elements[i] < Min_Element:
        Min_Element=Array_Elements[i]
print("Minimum Element from Array", Min_Element)

#Approch2
Array_Elements= [1,4,3,2,6,9,4,512,43]
print(min(Array_Elements))