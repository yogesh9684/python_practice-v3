# Fibonacci Series is the Addition of Previous two Numbers
# initial Default Value 0 and 1

Num1= 0
Num2= 1
print(Num1)
print(Num2)

for i in range(1 , 10 ):
    sum = Num1 + Num2
    print(sum)
    Num1 = Num2
    Num2 = sum
    sum = Num1
