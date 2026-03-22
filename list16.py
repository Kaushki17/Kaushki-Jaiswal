# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 16
# Stores marks of 5 students  in a list and calculate the average marks.

marks = [75,82,90,68,85]
total = 0
for m in marks:
    total += m
average = total/ len(marks)
print("Average marks:",average)