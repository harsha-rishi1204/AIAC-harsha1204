# Multiplication table generator

# Version 1: Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Version 2: Dynamic multiplication table generator
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Explanation:
# The first version always prints the table for 5.
# The second version prompts the user for a number and prints its table, making the program flexible and interactive.
# Re-prompting improved the solution by allowing the user to generate tables for any number, not just 5.