string_word = input("enter the string:\n")
for char in string_word:
    if string_word.count(char) == 1:
        print("string word have :" ,char)
