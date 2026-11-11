
print("Hello Learner!!\n")

while True:
    num = int(input("What is your number?\n"))

    take = input(
        "Do you want the multiplication table up to 10? ('y'/'Y' for yes, 'n'/'N' for no):\n"
    ).strip().lower()

    if take in ('y', 'Y'):
        mul = 10

    elif take in ('n', 'N'):
        mul = int(input("How many multipliers do you want?\n"))

    else:
        print("Your command is not accepted. Run again!\n")
        continue

    print(f"\nThe Multiplication Table of {num} upto {mul}:\n")

    for i in range(1, mul + 1):
        print(f"{num} x {i} = {num * i}")

    choice = input(
        "\nDo you want to see another table? ('y'/'Y' for yes, 'n'/'N' for no):\n"
    ).strip().lower()

    if choice in ('y', 'Y'):
        continue

    elif choice in ('n', 'N'):
        break

    else:
        print("Your command is not accepted. Exiting...")
        break

print("\nGreat Learning!")
