# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 15
# A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)


temperatures = [32, 36, 34, 38, 30, 37, 33]
hot_days = 0

for temp in temperatures:
    if temp > 35:
        hot_days += 1

print("Number of hot days:", hot_days)