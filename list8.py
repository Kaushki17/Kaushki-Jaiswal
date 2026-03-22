# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 8
# Given a list of numbers 1-20,creat a new list that contains only the even numbers.

numbers = list(range(1,21))
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)