import Database
import math
import pandas as pd
from Checking import Checking, Savings
from Service import CreditCard, Loan
from random import randint

class Handler():

    def __init__(self):
        '''
        Description:
            Initliazes Handler object.
        Parameters:
            No parameters.
        Returns:
            No returns.
        '''
        pass

    def confirm_user_type(self, db):
        '''
        Description:
            Confirms user login credentials as well as user type.
        Parameters:
            db (Database): A Database object.
        Returns:
            user_type (int): The user's type.
            username (str): The user's username.
        '''

        done = False

        while not done:
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            user_lst = list(db.df.username.astype(str))

            if username in user_lst:

                row = db.df[db.df['username'] == username]
                row_pass = row.password.item()


                if password == row_pass:
                    done = True
                else:
                    print('Invalid password.')
            else:
                print('Username not found.')

        user_type = 0

        if math.isnan(row.customer_id.item()) and math.isnan(row.employee_id):
            user_type = int(input("Continue as customer (1) or employee (2)? "))
        elif math.isnan(row.employee_id):
            user_type = 1
        else:
            user_type = 2
        return user_type, username

    def initialize_cust_objs(self, db, username):
        '''
        Description:
            Initializes the Customer object as well as its associated objects.
        Parameters:
            db (Database): A Database object.
            username (str): The user's username.
        Returns:
            objs_dict (dict): A dictionary containing objects associated with the customer.
        '''
        objs_dict = dict()
        row = db.df[db.df.username == username]
        objs_dict['customer'] = Customer(row.first_name.item(), row.last_name.item(), row.date_of_birth.item(), row.address.item(), row.customer_id.item())
        if not math.isnan(row.checking_acct_id):
            objs_dict['checking'] = Checking(row.checking_acct_id.item(), row.checking_acct_bal.item())
        if not math.isnan(row.savings_acct_id):
            objs_dict['savings'] = Savings(row.savings_acct_id.item(), row.savings_acct_bal.item())
        if not math.isnan(row.credit_card_id):
            objs_dict['credit_card'] = CreditCard(row.credit_card_id.item(), row.credit_card_limit.item(), row.credit_card_irate.item(), row.credit_card_bal.item())
        if not math.isnan(row.loan_id):
            objs_dict['loan'] = Loan(row.loan_id.item(), row.loan_limit.item(), row.loan_irate.item(), row.loan_bal.item())
        return objs_dict

    def initialize_emp_obj(self, db, username):
        '''
        Description:
            Initializes an Employee object associated with the user.
        Parameters:
            db (Database): The database object.
            username (str): The user's username.
        Returns:
            emp_obj (Employee): A user's employee object.
        '''
        row = db.df[db.df.username == username]
        emp_obj = Employee(row.first_name, row.last_name, row.date_of_birth, row.address, row.employee_id)
        return emp_obj

    def update_value(self, db, username, col, new_val):
        '''
        Description:
            Updates a value in the database.
        Parameters:
            db (Database): The database object.
            username (str): The user's username.
            col (str): The column in the database.
            new_val (str): The new value to enter.
        Returns:
            No returns.
        '''
        row = db.df[db.df.username == username]
        row[col] = new_val
        print('New ' + col + ' value is: ', row[col].item())

    def enter_new_user(self, db, user_type, new_id, fn, ln, dob, username, addr, password):
        '''
        Description:
            Enters a new user into the database.
        Parameters:
            db (Database): The database object.
            user_type (int): The user's type.
            new_id (str): The new user's ID number.
            fn (str): The new first name.
            ln (str): The new last name.
            dob (str): The new date of birth.
            username (str): The user's username.
            addr (str): The user's address.
            password (str): The user's password.
        Returns:
            No returns.
        '''
        cols = ['first_name', 'last_name', 'date_of_birth', 'username', 'address', 'password']

        if user_type == 1:
            cols.insert(0, 'customer_id')
        else:
            cols.insert(0, 'employee_id')

        db.df.loc[-1, cols] = [new_id, fn, ln, dob, username, addr, password]
        db.df.index += 1
        db.df = db.df.sort_index()

    def drop_user(self, db, username):
        '''
        Description:
            Deletes a user from the database.
        Parameters:
            db (Database): The database object.
            username (str): The user's username.
        Returns:
            No returns.
        '''
        user_list = list(db.df.username.astype(str))
        if username in user_list:
            to_delete = db.df[db.df['username'] == username].index
            db.df.drop(to_delete, inplace=True)
        else:
            print(username + " not in database.")

    def enter_new_account(self, db, option, username, checking_id, balance):
        '''
        Description:
            Updates a value in the database.
        Parameters:
            db (Database): The database object.
            option (int): The new account option (1 for checking, 2 for savings)
            username (str): The user's username.
            checking_id (str): The new account ID number.
            balance (int): The starting balance.
        Returns:
            No returns.
        '''
        if option == 1:
            db.df.loc[db.df['username'] == username, 'checking_acct_id'] = checking_id
            db.df.loc[db.df['username'] == username, 'checking_acct_bal'] = balance
        else:
            db.df.loc[db.df['username'] == username, 'savings_acct_id'] = checking_id
            db.df.loc[db.df['username'] == username, 'savings_acct_bal'] = balance

    def enter_new_service(self, db, option, username, new_id, limit, interest_rate, balance):
        '''
        Description:
            Updates a value in the database.
        Parameters:
            db (Database): The database object.
            option (int): The new account option (1 for credit card, 2 for loan)
            username (str): The user's username.
            new_id (str): The new account number for the service.
            limit (str): The new service limit.
            interest_rate (str): The new interest rate.
            balance (int): The starting balance.
        Returns:
            No returns.
        '''
        if option == 1:
            db.df.loc[db.df['username'] == username, 'credit_card_id'] = new_id
            db.df.loc[db.df['username'] == username, 'credit_card_limit'] = limit
            db.df.loc[db.df['username'] == username, 'credit_card_irate'] = interest_rate
            db.df.loc[db.df['username'] == username, 'credit_card_bal'] = balance
        else:
            db.df.loc[db.df['username'] == username, 'loan_id'] = new_id
            db.df.loc[db.df['username'] == username, 'loan_limit'] = limit
            db.df.loc[db.df['username'] == username, 'loan_irate'] = interest_rate
            db.df.loc[db.df['username'] == username, 'loan_bal'] = balance

    def update_csv(self, db):
        '''
        Description:
            Calls the database function to write its data to a csv file.
        Parameters:
            db (Database): The database object.
        Returns:
            No returns.
        '''
        db.db_to_csv('data.csv')


class User:

    def __init__(self, fn, ln, dob, addr):
        '''
        Description:
            Initializes the User object.
        Parameters:
            meters:
            fn (str): The new first name.
            ln (str): The new last name.
            dob (str): The new date of birth.
            addr (str): The new address.
        Returns:
            No returns.
        '''
        self.first_name = fn
        self.last_name = ln
        self.date_of_birth = dob
        self.address = addr

    def set_first_name(self, fn):
        '''
        Description:
            Sets the first name to a new value.
        Parameters:
            fn (str): The new first name value.
        Returns:
            No returns.
        '''
        self.first_name = fn

    def set_last_name(self, ln):
        '''
        Description:
            Sets last name to new value.
        Parameters:
            ln (str): The new last name.
        Returns:
            No returns.
        '''
        self.last_name = ln

    def set_dob(self, dob):
        '''
        Description:
            Sets dob to new value.
        Parameters:
            dob (str): The new dob value.
        Returns:
            No returns.
        '''
        self.date_of_birth = dob

    def set_address(self, addr):
        '''
        Description:
            Sets address to new value.
        Parameters:
            addr (str): The new address value.
        Returns:
            No returns.
        '''
        self.address = addr

    def get_first_name(self):
        '''
        Description:
            Returns first name.
        Parameters:
            No parameters.
        Returns:
            first_name (str): The first name of the user.
        '''
        return self.first_name

    def get_last_name(self):
        '''
        Description:
            Returns last name.
        Parameters:
            No parameters.
        Returns:
            last_name (str): The last name of the user.
        '''
        return self.last_name

    def get_dob(self):
        '''
        Description:
            Returns dob of the user.
        Parameters:
            No parameters.
        Returns:
            date_of_birth (str): The user's date of birth.
        '''
        return self.date_of_birth

    def get_address(self):
        '''
        Description:
            Returns the user's address.
        Parameters:
            No parameters.
        Returns:
            address (str): The user's address.
        '''
        return self.address


class Customer(User):

    def __init__(self, fn, ln, dob, addr, cust_id):
        '''
        Description:
            Initliazes the Customer object.
        Parameters:
            fn (str): The new first name.
            ln (str): The new last name.
            dob (str): The new date of birth.
            address (str): The new address.
            cust_id (str): The new customer ID number.
        Returns:
            No returns.
        '''
        User.__init__(self, fn, ln, dob, addr)
        self.customer_id = cust_id

    def set_customer_id(self, cust_id):
        '''
        Description:
            Sets the customer ID to a new value.
        Parameters:
            cust_id (str): The new customer ID value.
        Returns:
            No returns.
        '''
        self.customer_id = cust_id

    def get_customer_id(self):
        '''
        Description:
            Returns the customer ID value.
        Parameters:
            No parameters.
        Returns:
            customer_id (str): The customer ID number.
        '''
        return self.customer_id


class Employee(User):

    def __init__(self, fn, ln, dob, address, emp_id):
        '''
        Description:
            Initliazes the Employee object.
        Parameters:
            fn (str): The new first name.
            ln (str): The new last name.
            dob (str): The new date of birth.
            address (str): The new address.
            emp_id (str): The new employee ID.
        Returns:
            No returns.
        '''
        User.__init__(self, fn, ln, dob, address)
        self.employee_id = emp_id

    def set_employee_id(self, emp_id):
        '''
        Description:
            Sets the employee ID to a new value.
        Parameters:
            emp_id (str): The new employee ID.
        Returns:
            No returns.
        '''
        self.employee_id = emp_id

    def get_employee_id(self):
        '''
        Description:
            Returns the employee ID.
        Parameters:
            No parameters.
        Returns:
            employee_id (str): The employee ID number.
        '''
        return self.employee_id

    def create_new_user(self, db, db_handler):
        '''
        Description:
            Creates a new user for entry into the database.
        Parameters:
            db (Database): A Database object.
            db_handler (Handler): A Handler object.
        Returns:
            No returns.
        '''
        first_name, last_name = input('Enter first and last name: ').split()
        address = input('Enter address: ')
        dob = input('Enter date of birth in mm/dd/yyyy format: ')
        username = input('Enter new username: ')
        password = input('Enter new password: ')
        user_type = int(input('New customer (1) or employee (2)? '))
        new_id = randint(100000, 999999)
        db_handler.enter_new_user(db, user_type, new_id, first_name, last_name, dob, username, address, password)

    def delete_user(self, db, db_handler):
        '''
        Description:
            Deletes a user from the database and all associated accounts.
        Parameters:
            db (Database): A Database object.
            db_handler (Handler): A Handler object.
        Returns:
            No returns.
        '''
        username = input('Enter username of user to delete: ')
        option = input('Are you sure you want to delete this user? (y/n) ')
        if option == 'y':
            db_handler.drop_user(db, username)

    def create_new_account(self, db, db_handler):
        '''
        Description:
            Creates a new checking or savings account for the user.
        Parameters:
            db (Database): A Database object.
            db_handler (Handler): A Handler object.
        Returns:
            No returns.
        '''
        option = int(input('Create new checking (1) or savings (2) account? '))
        username = input('Enter customer\'s username: ')
        checking_id = randint(100000000, 999999999)
        balance = float(input("Enter starting balance: "))
        db_handler.enter_new_account(db, option, username, checking_id, balance)

    def create_new_service(self, db, db_handler):
        '''
        Description:
            Creates a new credit card or loan account for the user.
        Parameters:
            db (Database): A Database object.
            db_handler (Handler): A Handler object.
        Returns:
            No returns.
        '''
        option = int(input('Create credit card (1) or loan (2) account? '))
        username = input('Enter customer\'s username: ')
        new_id = randint(100000000, 999999999)
        limit = float(input('Enter service limit: '))
        interest_rate = float(input('Enter interest rate: '))
        balance = 0
        db_handler.enter_new_service(db, option, username, new_id, limit, interest_rate, balance)