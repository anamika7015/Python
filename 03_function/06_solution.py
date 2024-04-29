num1 = int(input("enter the number:\n"))
num2 = int(input("enter the number:\n"))
num_x = int(input("enter the number:\n"))
def sum_of_two_number(num1,num2):
    result = num1+num2
    return result
result = sum_of_two_number(num1,num2)
print("sum of  two number",result)

cube = lambda x: x**3
print("cube  of", num_x,"is",cube(num_x))