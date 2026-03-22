# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 21
# A teacher stores marks of students in a listmarks = [78, 65, 89, 90, 56]Write a program to:Print all marksFind total marksFind average marksFind highest marks Find lowest marks


marks = [78, 65, 89, 90, 56]
print("Marks:", marks)

total = sum(marks)
print("Total marks:", total)

average = total / len(marks)
print("Average marks:", average)

highest = max(marks)
print("Highest marks:", highest)

lowest = min(marks)
print("Lowest marks:", lowest)