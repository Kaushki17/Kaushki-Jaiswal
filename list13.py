# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 13
# Create alist of ages.Create two new lists : minors(under 18) and adults(18 and above)

ages = [12,17,43,21,25,30,16]
minors = []
adults = []
for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)
print("Minors: ",minors)
print("Adults: ",adults)