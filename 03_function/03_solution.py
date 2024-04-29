character = input("enter the character\n")
number = int(input("enter the number\n"))
def character_multiply(character,number):
   result = (character +" ") * number
   return result
multiply = character_multiply(character,number)
print(multiply)