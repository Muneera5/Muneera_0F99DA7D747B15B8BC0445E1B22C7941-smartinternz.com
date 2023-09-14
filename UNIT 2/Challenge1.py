"""
Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 


"""
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount:.2f} into the account.")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount:.2f} from the account.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder Name: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance:.2f}")


# Example usage:
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_account = BankAccount("33330699", "Sam", 3000.0)

    # Test deposit and withdrawal functionality
    my_account.display_balance()
    my_account.deposit(800.0)
    my_account.withdraw(300.0)
    my_account.display_balance()