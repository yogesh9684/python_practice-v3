
#Approch 1
String = " Welcome to World of Python Programming"
SubString = "Python"

print(String.find(SubString))

if String.find(SubString) == -1:
    print("Substring is not present")
else:
    print("Substring is present")

#Approch 2

String = " Welcome to World of Python Programming"
SubString = "Welcome"

if SubString in String:
    print("Substring is Present")
else:
    print("Substring is Not Present")
