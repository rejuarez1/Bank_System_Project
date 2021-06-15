import os.path
import pandas as pd
from os import path

class Database:

    def __init__(self, file):
        '''
        Description:
            Initializes Database object.
        Parameters:
            file (str): The file path of the database document.
        Returns:
            No return.
        '''
        if path.exists(file):
            self.df = pd.read_csv(file)
        else:
            cols = ['customer_id', 'employee_id', 'first_name', 'last_name', 'date_of_birth', 'address', 'username', 'password',
            'checking_acct_id', 'checking_acct_bal', 'savings_acct_id', 'savings_acct_bal',
            'credit_card_id', 'credit_card_limit', 'credit_card_irate', 'credit_card_bal',
            'loan_id', 'loan_limit', 'loan_irate', 'loan_bal', 'datetime']
            self.df = pd.DataFrame(columns = cols)
            self.df.loc[1,'username'] = 'admin'
            self.df.loc[1,'password'] = 'admin'
            self.df.loc[1, 'employee_id'] = '000000'
            self.df.to_csv(file)

    def db_to_csv(self, file):
        '''
        Description:
            Writes the updated database to a csv file.
        Parameters:
            file (str): The file path where the database will be written.
        Returns:
           No return.
        '''
        self.df.to_csv(file, index=False)