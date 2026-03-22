# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 5
# Create a list of 10 random integer. Use  a for loop to print each other number multiplied by 2.

import random
numbers = []
for i in range(10):
  numbers.append(random.randint(1,50))
print(numbers)
for num in numbers:
    print(num*2)