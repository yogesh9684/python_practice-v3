MyString = "YOGESH DIPAKRAO SAWANT"
MyWords = MyString.split(" ")
print(MyWords)
MyNewWord= MyWords[-1::-1]
print(MyNewWord)
OutputString = " ".join(MyNewWord)
print(OutputString)
