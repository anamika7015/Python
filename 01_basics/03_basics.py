marks1 = float(input("enter the number1:\n"))
marks2 = float(input("enter the number2:\n"))
activities1 = float(input(" enter the activities1:\n"))
activities2 = float(input(" enter the activities2:\n"))
activities3 = float(input(" enter the activities3:\n"))
sports = float(input("enter the number:\n"))
avg = (marks1 + marks2) / 2
activities = (activities1 + activities2 + activities3) / 3
weight_marks = avg * 0.50
weight_activities = activities * 0.20
weight_sports = sports * 0.30
result = weight_marks + weight_activities + weight_sports
print(result)

