while True:
    fruit_color = input("Enter the fruit color:\n")
    print(fruit_color)
    if fruit_color == "green":
        print("fruits is unripe")
    elif fruit_color == "yellow":
        print("fruit is ripe")  
    elif fruit_color == "brown":
        print("fruit is overripe") 
    else:
        print("invalid fruit color please mention anyone of these three types green, yellow,brown")    

 