#Factorial Number Stands Like 5 = 5*4*3*2*1
# Factorial of 0 is always 1
# Factorial of Negative Number Does not Exist

#Approch 1

Num = 5
Factorial = 1

for i in range(1 , Num+1):
    Factorial = Factorial * i
print("Factorial of Number", Num , "is" ,Factorial)


#Approch 2
#Factorial using Recursive Function

def fact(num):
    if num > 1:
        num = num*fact(num-1)

    return num
num =5
print(fact(num))