# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 23
# A cricket player scored runs in 6 matches.Example: [45, 60, 10, 80, 55, 90] Write a program to:Find total runsFind highest score Count how many matches player scored more than 50 runs

runs = [45, 60, 10, 80, 55, 90]

# Total runs
total_runs = sum(runs)
print("Total runs:", total_runs)

# Highest score
highest = max(runs)
print("Highest score:", highest)

# Count matches with runs more than 50
count = 0
for r in runs:
    if r > 50:
        count = count + 1

print("Matches with more than 50 runs:", count)