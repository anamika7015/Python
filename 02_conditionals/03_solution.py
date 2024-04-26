while True:
    score = int(input("enter your score"))
    if score>=101:
        print("invalid number")
        exit()
    if score >=90:
        print("grade A")
    elif score>=80:
        print("grade B")
    elif score>=70:
        print("grade C")
    elif score>=60:
        print("grade D")
    elif score<60:
        print("grade E")
    else:
        print("Invalid numbers")    

        