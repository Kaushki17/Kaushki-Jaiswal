# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 10
# Given a list of 10 student marks,count how many students scored above 40.

marks = [34,67,88,95,45,76,56,33,67,55]
count = 0
for i in marks:
    if i > 40:
        count += 1
print("Students who scored above 40: ",count)