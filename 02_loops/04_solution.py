# price of movie ticket


Day = input("enter the day")
age = int(input("enter the age"))
#   method 1
price = 12 if age>=18 else 8
if Day == "wednesday":
   price -= 2
   print("your movie ticket price is:",price)

 
      
