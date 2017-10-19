# Functions and Variables
# variables in function are not connected to variables in script

# define function that accepts 2 aruguments and returns statements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# pass numbers as arguments cheese_and_crackers function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# pass cheese_and_crackers function variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# pass mathematical expressions as arguments to function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# pass variables and mathematical expressions as arguments to function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
