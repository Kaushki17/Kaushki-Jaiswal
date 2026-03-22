# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 12
# calculate the sum of all element in a list without using sum9 function (use a loop and a tracksr variable.)

numbers = [34,26,37,43,55]
total = 0
for num in numbers:
      total = total+num
print("Total marks: ",total)


numbers = [34,26,37,43,55]
total = 0
count = 0
for num in numbers:
    if num >= 40:
      total = total+num
      count = count+1
print("Avg marks: ",total/count)

