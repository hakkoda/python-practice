# Write a program to read a positive integer N and determine 
#   a) whether N is even or odd
#   b) whether or not N is prime
#   c) whether or not N is a perfect square

# TODO: need to right function to find perfect square

print("""
This program will take a positive integer and determine if it is even/odd,
prime, or a perfect square.  Enter a negative number to end program.
""")

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False

    return True

def is_perfect_square(num):
    for x in range(2, num):
        square = x * x
        if square == num:
            return True
        elif square > num:
            return False

    return False

num = 0
while num > -1:
    num = input("Enter a positive integer> ")
    num = int(num)

    if num < 0:
        break

    is_num_even = is_even(num)
    is_num_prime = is_prime(num)
    is_num_perfect_square = is_perfect_square(num)

    print(f"{num} is even: {is_num_even}")
    print(f"{num} is prime: {is_num_prime}")
    print(f"{num} is perfect square: {is_num_perfect_square}")
