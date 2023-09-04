# Approch 1

# List = [12,32,12,45,33,12,55,54,12,30,12,34,12]
# count = 0
#
# for i in List:
#     if i == 12:
#         count = count +1
# print("Number",i,"Occoured",count,"Times in List")

#Approch 2

List = [12,32,12,45,33,12,55,54,12,30,12,34,12]
Number = int(input("Enter the Number of your choice="))
if Number in List:
    Test= List.count(Number)
    print(Test)
else:
    print("Number is not available in List")



