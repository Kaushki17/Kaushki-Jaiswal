# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 9
# Write a program that takes a list of names and a "search_name" from the user.Print the index where the name is founf,or not found.

names = ["Aman","Riya","Suhani","Priya","Rahul"]
search_name = input("Enter a name to search: ")
if search_name in names:
    print("Found :",names.index(search_name))
else:
    print("Not found")