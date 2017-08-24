# numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 10
# print(numbers)
#
# numbers[6] = 1
# print(numbers)

# print(numbers[2:])

# print(9 in numbers)

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


# def main():
#     """Display income report for incomes over a given number of months."""
#     incomes = []
#     number_of_months = int(input("How many months? "))
#
#     for month in range(1, number_of_months + 1):
#         income = float(input("Enter income for month: ".format(month)))
#         incomes.append(income)
#
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, number_of_months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
#
#
# main()

# def main():
#     """Display different versions of input data"""
#     numbers = []
#
#     for i in range(5):
#         number = int(input("number: ".format(i)))
#         numbers.append(number)
#
#     if sum(numbers) >= 10:
#         print("large")
#     else:
#         print("small")
#
# main()

# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
#
# if str(input("username: ")) in usernames:
#     print("access granted")
#
# else:
#     print("access denied")

"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing tuples of both initials
# splits each name and adds the first letter of each part to a tuple
full_initials = [(name.split()[0][0], name.split()[1][0]) for name in
                 full_names]
print(full_initials)

almost_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# TODO: use a list comprehension to create a list of integers
# from this list of strings
# numbers =

# TODO: use a list comprehension to create a list of all of the full_names
# in lowercase format
# lowercase_full_names =
