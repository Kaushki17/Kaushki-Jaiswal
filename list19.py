# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 19
# A teacher stored attendance of students in a list (1 = present, 0 = absent).Example: [1,1,0,1,0,1,1]Write a program to:Count total presentCount total absentPrint attendance percentage


attendance = [1, 1, 0, 1, 0, 1, 1]
present = attendance.count(1)
absent = attendance.count(0)
percentage = (present / len(attendance)) * 100
print("Total Present:", present)
print("Total Absent:", absent)
print("Attendance Percentage:", percentage, "%")