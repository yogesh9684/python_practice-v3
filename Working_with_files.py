
# How to WRITE to A File

# List = ["Yogesh ","Dipakrao ","Sawant"]
# MyFile =open("E:\workspace_python\Basic_Programs_Pythons\sample_working.txt","w")
# for item in List:
#     MyFile.write(str(item))
# print("File has been written")
# MyFile.close()

# How to READ a File

# MyFile = open("E:\workspace_python\Basic_Programs_Pythons\sample_working.txt",'r')
# print(str(MyFile.read()))
# MyFile.close()

# It will Just read the Single line of the File
MyFile = open("/Basic_Programs_Pythons\sample_working.txt", 'r')
print(str(MyFile.readline()))
MyFile.close()
