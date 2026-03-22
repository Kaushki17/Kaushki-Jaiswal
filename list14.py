# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 14
# Store prices of 5 items in a list. Calculate the total bill and the average price per item.

# Store prices of 5 items
prices = [120, 250, 80, 150, 200]
total = 0
for price in prices:
    total = total + price
average = total / len(prices)

print("Total Bill:", total)
print("Average Price per Item:", average)