import os
import time

class Calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def modulus(self, x, y):
        return x % y

    def exponentiation(self, x, y):
        return x ** y

    def floor_division(self, x, y):
        return x // y

    def calculate(self):
        os.system("clear")
        print("""
 _____________________
|  _________________  |
| | FW  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |% |**|//|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
        print("""
★★★★★★★★★★★★★★★ Calculator ★★★★★★★★★★★★★★★
★                                        ★
★   Enter 0 to exit                      ★
★   Enter 1 for addition                 ★
★   Enter 2 for subtraction              ★
★   Enter 3 for multiplication           ★
★   Enter 4 for division                 ★
★   Enter 5 for modulus                  ★
★   Enter 6 for exponentiation           ★
★   Enter 7 for floor division           ★
★                                        ★
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
""")
        
        while True:
            try:
                choice = input("Select an operation: ").strip()
                if choice == "0":
                    [print("." * i) or time.sleep(0.1) for i in range(1, 10)]
                    print("Exited the calculator...")
                    exit()
                elif choice in {"1", "2", "3", "4", "5", "6", "7"}:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                    if choice == "1":
                        print(num1, "+", num2, "=", self.addition(num1, num2))
                    elif choice == "2":
                        print(num1, "-", num2, "=", self.subtraction(num1, num2))
                    elif choice == "3":
                        print(num1, "*", num2, "=", self.multiplication(num1, num2))
                    elif choice == "4":
                        print(num1, "/", num2, "=", self.division(num1, num2))
                    elif choice == "5":
                        print(num1, "%", num2, "=", self.modulus(num1, num2))
                    elif choice == "6":
                        print(num1, "**", num2, "=", self.exponentiation(num1, num2))
                    elif choice == "7":
                        print(num1, "//", num2, "=", self.floor_division(num1, num2))
                    exit_choice = input("Press enter to continue or type 0 to exit: ").strip()
                    if exit_choice.lower() == "0":
                        exit()
                else:
                    print("Selection an option from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue


if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculate()