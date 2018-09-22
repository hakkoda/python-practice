def my_loop(end):
    i = 0
    numbers = []

    while i < end:
        #print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        #print("Numbers now: ", numbers)
        #print(f"At the bottom i is {i}")

    print("The numbers:", end=" ")
    for num in numbers:
        print(num, end=" ")
    print()

stop_program = "yes"
while stop_program.lower().startswith("y"):
    the_end = input("Enter the stopping value > ")
    the_end = int(the_end)
    my_loop(the_end)
    stop_program = input("Do it again (yes, no): ")
