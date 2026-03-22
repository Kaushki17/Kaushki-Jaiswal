# Program by : Kaushki Jaiswal
# Roll no: 35
# List assignment : 7
# Ask a user for a fruit name. Check if it exist in your fruit_basket list using the im keyword.

fruit_basket = ["Apple","Mango","Papaya","Orange","Grapes"]
fruit = input("Enter a fruit name: ")
if fruit in fruit_basket:
    print("Fruit is in the basket.")
else:
    print("Fruit is not in the basket.")