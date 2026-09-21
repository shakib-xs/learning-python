# Python Encapsulation
#
# Encapsulation keeps data and methods together
# and can restrict direct access to internal data.
#
# A double underscore (__) is commonly used
# for name-mangled private attributes.
#
# Syntax:
# self.__variable = value


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

print(account.get_balance())
