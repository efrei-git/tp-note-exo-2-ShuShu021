from functions import *

def menu():
    print("\n==== Menu ====")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Exit")
    print("**Only supports integer input**")

while True:
    menu()
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        num = int(input("Enter a number: "))
        fact = factorial(num)
        print("Factorial of", num, "is", fact)
    elif choice == '2':
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

