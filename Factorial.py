class Factorial:
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Error: Integer is non-positive!")

    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of ", number, " is ",factorial)
