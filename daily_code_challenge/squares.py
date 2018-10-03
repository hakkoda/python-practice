# Write a program which requests two integers, m and n, and produces a table of
# squares from m to n, inclusive.

print("Create a table of squares from m to n.")

m = input("Enter value for m > ")
m = int(m)

n = input("Enter value for n > ")
n = int(n)

for x in range(m, n+1):
    square = x * x
    print(f"{x} * {x} = {square}")
