# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 22
# Marks of students are stored in a list.marks = [78, 35, 90, 40, 55]Write a program to:Print PASS if marks ≥ 40 Print FAIL if marks < 40 Count how many students passed

marks = [78,35,90,40,55]
pass_count = 0
for m in marks:
    if m >= 40:
        print(m,"PASS")
        pass_count = pass_count + 1
    else:
        print(m,"FAIL")
print("Total students passed: ",pass_count)