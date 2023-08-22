#Number is divisible by itself and  1
#Number is Natural Number and has only 2 factor


#num = int(input("Enter the Number="))
num =-5
count = 0

if num > 1:
    for i in range(1,num+1):
        if num % i ==0:
            count=count+1
    if count == 2:
        print("Number is Prime")
    else:
        print("Number is not Prime")
else:
    print("Number is not Prime Number")