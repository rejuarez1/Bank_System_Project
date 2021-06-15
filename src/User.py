import Handler
from random import randint


class User:

    def __init__(self, fn, ln, dob, addr):
        '''
        '''
        self.first_name = fn
        self.last_name = ln
        self.date_of_birth = dob
        self.address = addr

    def set_first_name(self, fn):
        '''
        '''
        self.first_name = fn

    def set_last_name(self, ln):
        '''
        '''
        self.last_name = ln

    def set_dob(self, dob):
        '''
        '''
        self.date_of_birth = dob

    def set_address(self, addr):
        '''
        '''
        self.address = addr

    def get_first_name(self):
        '''
        '''
        return self.first_name

    def get_last_name(self):
        '''
        '''
        return self.last_name

    def get_dob(self):
        '''
        '''
        return self.date_of_birth

    def get_address(self):
        '''
        '''
        return self.address


class Customer(User):

    def __init__(self, fn, ln, dob, addr, cust_id):
        '''
        '''
        User.__init__(self, fn, ln, dob, addr)
        self.customer_id = cust_id

    def set_customer_id(self, cust_id):
        '''
        '''
        self.customer_id = cust_id

    def get_customer_id(self):
        '''
        '''
        return self.customer_id


class Employee(User):

    def __init__(self, fn, ln, dob, address, emp_id):
        '''
        '''
        User.__init__(self, fn, ln, dob, address)
        self.employee_id = emp_id

    def set_employee_id(self, emp_id):
        '''
        '''
        self.employee_id = emp_id

    def get_employee_id(self):
        '''
        '''
        return self.employee_id

    def create_new_user(self, db, db_handler):
        '''
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
        '''
        username = input('Enter username of user to delete: ')
        option = input('Are you sure you want to delete this user? (y/n) ')
        if option == 'y':
            db_handler.drop_user(db, username)

    def create_new_account(self, db, db_handler):
        '''
        '''
        option = int(input('Create new checking (1) or savings (2) account? '))
        username = input('Enter customer\'s username: ')
        checking_id = randint(100000000, 999999999)
        balance = float(input("Enter starting balance: "))
        db_handler.enter_new_account(db, option, username, checking_id, balance)

    def create_new_service(self, db, db_handler):
        '''
        '''
        option = int(input('Create credit card (1) or loan (2) account? '))
        username = input('Enter customer\'s username: ')
        new_id = randint(100000000, 999999999)
        limit = float(input('Enter service limit: '))
        interest_rate = float(input('Enter interest rate: '))
        balance = 0
        db_handler.enter_new_service(db, option, username, new_id, limit, interest_rate, balance)