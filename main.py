import math

print("Enter First Number.")
first = int(input("> "))
print("Enter Second Number.")
second = int(input("> "))
print("+ - * / Enter Operator")
operator = input("> ")

if operator == "+":
    print(first + second)
if operator == "-":
    print(first - second)
if operator == "*":
    print(first * second)
if operator == "/":
    print(first / second)
