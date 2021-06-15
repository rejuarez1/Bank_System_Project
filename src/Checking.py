class Checking:

    def __init__(self, acc_id, bal=0):
        '''
        Description:
            Initializes Checking object.
        Parameters:
            acc_id (str): The new checking account ID number.
            bal (int): The new starting balance, default value is 0.
        Returns:
            No returns.
        '''
        self.account_id = acc_id
        self.balance = bal

    def set_account_id(self, acc_id):
        '''
        Description:
            Sets account ID to new value.
        Parameters:
            acc_id (str): The new checking account ID number.
        Returns:
            No returns
        '''
        self.account_id = acc_id

    def set_balance(self, bal):
        '''
        Description:
            Sets balance to a new value.
        Parameters:
            bal (int): The new balance value.
        Returns:
            No returns.
        '''
        self.balance = bal

    def get_account_id(self):
        '''
        Description:
            Returns the account ID.
        Parameters:
            No parameters.
        Returns:
            account_id (str): The account ID number.
        '''
        return self.account_id

    def get_balance(self):
        '''
        Description:
            Returns the account balance.
        Parameters:
            No parameters
        Returns:
            balance (int): The account balance.
        '''
        return self.balance


    def withdraw(self, amount):
        '''
        Description:
            Withraws an amount from the account balance.
        Parameters:
            amount (int): The amount to withdraw.
        Returns:
            balance (int): The new account balance.
        '''
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Error: Withdraw amount exceeds current balance.")
        return self.balance

    def deposit(self, amount):
        '''
        Description:
            Deposits an amount into the account balance.
        Parameters:
            amount (int): The amount to deposit into the account.
        Returns:
            balance (int): The updated account balance.
        '''
        self.balance += amount
        return self.balance

    def transfer(self, other_account, amount):
        '''
        Description:
            Transfers an amount from one account to another account.
        Parameters:
            other_account (Checking/Savings): The other account where the transfer will go into.
            amount (int): The amount to transfer into the other account.
        Returns:
            balance (int): The updated account balance.
        '''
        new_balance = self.withdraw(amount)
        new_other_balance = other_account.deposit(amount)
        print("Transfer of ${} to account {} processed successfully.".format(amount, other_account.get_account_id()))
        print("New balance: {}".format(new_balance))
        print("New other account balance: {}".format(new_other_balance))


class Savings(Checking):

    def __init__(self, acc_id, bal=0):
        '''
        Description:
            Initializes Savings object.
        Parameters:
            acc_id (str): The new savings account ID number.
            bal (int): The new starting balance, default value is 0.
        Returns:
            No returns.
        '''
        Checking.__init__(self, acc_id, bal)
        self.daily_limit = 200
        self.interest_rate = .005

    def apply_interest(self):
        '''
        Description:
            Applies interest to the balance amount.
        Parameters:
            No parameters.
        Returns:
            No returns.
        '''
        self.balance += (self.balance * self.interest_rate)