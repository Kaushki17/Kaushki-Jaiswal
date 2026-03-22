# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 11
# Take a list like (-5,3,-2,8).Create a new list where all negative numbers are converted in positive.

numbers = [-5,3,-2,8]
positive_numbers = []
for num in numbers:
    if num < 0:
        positive_numbers.append(-num)
    else:
        positive_numbers.append(num)
print(positive_numbers)