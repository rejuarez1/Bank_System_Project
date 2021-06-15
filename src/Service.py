class Service:

    def __init__(self, serv_id, limit):
        '''
        Description:
            Initializes Service object.

        Parameters:
            serv_id (str): The service ID number.
            limit (str): The service limit number.

        Returns:
            No return.
        '''
        self.service_id = serv_id
        self.limit = limit

    def set_service_id(self, serv_id):
        '''
        Description:
            Sets service ID to new value.

        Parameters:
            serv_id (str): The new service ID number.

        Returns:
            No return.
        '''
        self.service_id = serv_id

    def set_limit(self, limit):
        '''
        Description:
            Sets service limit to new value.

        Parameters:
            limit (str): The new service limit number.

        Returns:
            No return.
        '''
        self.limit = limit

    def get_service_id(self):
        '''
        Description:
            Returns service id number.

        Parameters:
            No parameters.

        Returns:
            service_id (str): The service ID number.
        '''
        return self.service_id

    def get_limit(self):
        '''
        Description:
            Returns service limit number.

        Parameters:
            No parameters.

        Returns:
            limit (str): The service limit number.
        '''
        return self.limit


class CreditCard(Service):

    def __init__(self, serv_id, limit, interest_rate, balance = 0):
        '''
        Description:
            Initializes CreditCard object.

        Parameters:
            serv_id (str): The new service ID number.
            limit (str): The new limit number.
            interest_rate (str): The new interest rate.
            balance (int): The new balance. Default value is 0.

        Returns:
            No return.
        '''
        Service.__init__(self, serv_id, limit)
        self.interest_rate = interest_rate
        self.balance = balance

    def set_balance(self, bal):
        '''
        Description:
            Sets balance to new balance value.
        Parameters:
            bal (int): The new balance value.
        Returns:
            No return.
        '''
        self.balance = bal

    def set_limit(self, limit):
        '''
        Description:
            Sets limit to new limit value.
        Parameters:
            limit (str): The new limit value.
        Returns:
           No return.
        '''
        self.limit = limit

    def get_balance(self):
        '''
        Description:
            Returns balance.
        Parameters:
            No parameters.
        Returns:
            balance (int): The credit card balance.
        '''
        return self.balance

    def get_limit(self):
        '''
        Description:
            Returns the credit card limit.
        Parameters:
            No parameters.
        Returns:
            limit (int): The credit card limit.
        '''
        return self.limit

    def make_payment(self, amount):
        '''
        Description:
            Makes a payment on the credit card balance.
        Parameters:
            amount (int): The amount to subtract from the credit card balance.
        Returns:
            balance (int): The updated credit card balance.
        '''
        self.balance -= amount
        return self.balance

    def make_transaction(self, amount):
        '''
        Description:
            Makes a transaction on the credit card.
        Parameters:
            amount (int): The amount to add to the credit card balance.
        Returns:
            balance (int): The updated credit card balance.
        '''
        if (amount + self.balance) <= self.limit:
            self.balance += amount
        else:
            print("Error: Amount exceeds available credit.")
        return self.balance

    def apply_interest(self):
        '''
        Description:
            Applies interest to the credit card balance.
        Parameters:
            No parameters.
        Returns:
           balance (int): The new balance amount.
        '''
        self.balance += (self.balance * interest_rate)
        return self.balance


class Loan(Service):

    def __init__(self, serv_id, limit, interest_rate, balance = 0):
        '''
        Description:
            Initializes the Loan object.
        Parameters:
            serv_id (int): The new loan service ID number.
            limit (int): The new loan limit number.
            interest_rate (int): The new loan interest rate.
            balance (int): The new loan balance, default value is 0.
        Returns:
            No return.
        '''
        Service.__init__(self, serv_id, limit)
        self.interest_rate = interest_rate
        self.balance = balance

    def get_balance(self):
        '''
         Description:
            Returns loan balance.
         Parameters:
            No parameters.
         Returns:
            balance (int): The loan balance.
        '''
        return self.balance

    def get_limit(self):
        '''
         Description:
            Returns the loan limit.
         Parameters:
            No parameters.
         Returns:
            limit (int): The loan limit.
        '''
        return self.limit

    def make_payment(self, amount):
        '''
        Description:
            Makes a payment on the loan balance.
        Parameters:
            amount (int): The amount to subtract from the loan balance.
        Returns:
            balance (int): The updated loan balance.
        '''
        self.balance -= amount
        return self.balance

    def apply_interest(self):
        '''
        Description:
            Applies interest to the loan balance.
        Parameters:
            No parameters.
        Returns:
           balance (int): The new balance amount.
        '''
        self.balance += (self.balance * interest_rate)
        return self.balance