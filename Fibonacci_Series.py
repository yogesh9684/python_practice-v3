# Fibonacci Series is the Addition of Previous two Numbers
# initial Default Value 0 and 1

num1= 0
num2= 1
print(num1)
print(num2)

for i in range(1 , 10 ):
    sum = num1 + num2
    print(sum)
    num1 = num2
    num2 = sum
    sum = num1
