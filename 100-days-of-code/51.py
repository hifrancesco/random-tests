### object-oriented programming ###
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2


# rectangle = Rectangle(5, 10)
# print("Area:", rectangle.area()) 
# print("Perimeter:", rectangle.perimeter())


### object-oriented programming ###
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} successful. New balance is {self.balance}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. New balance is {self.balance}."


# Create an instance of BankAccount
my_account = BankAccount("123456789", 1000)

# Call its methods
print(my_account.deposit(500))
print(my_account.withdraw(200))