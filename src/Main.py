import Checking
import Service
import logging
import pandas as pd
import numpy as np
from random import randint
from Database import Database
from Handler import Handler

def prompt_customer_menu():
    '''
    Description:
        Outputs a menu for the customer and prompts a response.
    Parameters:
        No parameters.
    Returns:
        choice (int): The choice the customer enters.
    '''
    print('Hello valued customer! Please select from the following options:')
    menu = '\n1.Checking\n2.Savings Account\n3.Credit Card\n4.Loan\n5.End session\n'
    choice = int(input(menu))
    while choice < 1 or choice > 5:
        choice = int(input('ERROR: Invalid input.' + menu))
    return choice

def prompt_employee_menu():
    '''
    Description:
        Outputs a menu for the employee and prompts a response.
    Parameters:
        No parameters.
    Returns:
        choice (int): The choice the employee enters.
    '''
    print('Hello valued employee! Please select from the following options:')
    menu = '\n1.Add/Remove Customer\n2.Create new customer banking account\n3.Create new customer service account\n4.End session\n'
    choice = int(input(menu))
    while choice < 1 or choice > 4:
        choice = int(input('ERROR: Invalid input.' + menu))
    return choice

def main():
    logging.basicConfig(level=logging.INFO)
    db = Database('data.csv')
    db_handler = Handler()

    user_type, user_name = db_handler.confirm_user_type(db)

    done = False
    if user_type == 1:
        cust_objs = db_handler.initialize_cust_objs(db, user_name)
        logging.info('\nThe customer object and its associated accounts have been initialized\n')
        while not done:
            customer_answer = prompt_customer_menu()

            if customer_answer == 1 or customer_answer == 2:
                action = int(input('\n1.Withdraw\n2.Deposit\n3.Transfer\n'))
                if customer_answer == 1:
                    if action == 1:
                        amt = float(input('Enter quantity to withdraw: '))
                        new_amt = cust_objs['checking'].withdraw(amt)
                        db_handler.update_value(db, user_name, 'checking_acct_bal', new_amt)
                        logging.info('\nThe withdrawal was successful.\n')
                    elif action == 2:
                        amt = float(input('Enter quantity to deposit: '))
                        new_amt = cust_objs['checking'].deposit(amt)
                        db_handler.update_value(db, user_name, 'checking_acct_bal', new_amt)
                        logging.info('\nThe deposit was successful.\n')
                    else:
                        amt = float(input('Enter transfer amount: '))
                        cust_objs['checking'].transfer(cust_objs['savings'], amt)
                        db_handler.update_value(db, user_name, 'checking_acct_bal', cust_objs['checking'].get_balance())
                        db_handler.update_value(db, user_name, 'savings_acct_bal', cust_objs['savings'].get_balance())
                        logging.info('\nThe transfer was successful.\n')

                else:
                    if action == 1:
                        amt = float(input('Enter quantity to withdraw: '))
                        new_amt = cust_objs['savings'].withdraw(amt)
                        db_handler.update_value(db, user_name, 'savings_acct_bal', new_amt)
                        logging.info('\nThe withdrawal was successful.\n')
                    elif action == 2:
                        amt = float(input('Enter quantity to deposit: '))
                        new_amt = cust_objs['savings'].deposit(amt)
                        db_handler.update_value(db, user_name, 'savings_acct_bal', new_amt)
                        logging.info('\nThe deposit was successful.\n')
                    else:
                        amt = float(input('Enter transfer amount: '))
                        cust_objs['savings'].transfer(cust_objs['checking'], amt)
                        db_handler.update_value(db, user_name, 'savings_acct_bal', cust_objs['savings'].get_balance())
                        db_handler.update_value(db, user_name, 'checking_acct_bal', cust_objs['checking'].get_balance())
                        logging.info('\nThe transfer was successful.\n')


            elif customer_answer == 3 or customer_answer == 4:
                action = int(input('\n1.Make payment\n2.Make Credit Card Transaction\n'))
                if action == 1:
                    amt = float(input('Enter payment amount: '))
                    if customer_answer == 3:
                        db_handler.update_value(db, user_name, 'credit_card_bal', cust_objs['credit_card'].make_payment(amt))
                        logging.info('\nThe payment was successful.\n')
                    else:
                        db_handler.update_value(db, user_name, 'loan_bal', cust_objs['loan'].make_payment(amt))
                        logging.info('\nThe payment was successful.\n')
                else:
                    amt = float(input('Enter amount to transact: '))
                    db_handler.update_value(db, user_name, 'credit_card_bal', cust_objs['credit_card'].make_transaction(amt))
                    logging.info('\nThe transaction was successful.\n')
            else:
                done = True
                print("Thank you for your business!\n")
                logging.info('\nThe customer session has concluded.\n')


    else:
        emp_obj = db_handler.initialize_emp_obj(db, user_name)
        while not done:
            option = prompt_employee_menu()

            if option == 1:
                option = int(input('Add new user (1) or remove existing user (2)? '))
                if option == 1:
                    emp_obj.create_new_user(db, db_handler)
                    logging.info('\nNew user successfully created.\n')
                elif option == 2:
                    emp_obj.delete_user(db, db_handler)
                    logging.info('\nNew user successfully deleted.\n')
            elif option == 2:
                emp_obj.create_new_account(db, db_handler)
                logging.info('\nNew account successfully created.\n')
            elif option == 3:
                emp_obj.create_new_service(db, db_handler)
                logging.info('\nNew service account successfully created.\n')
            elif option == 4:
                done = True

        print('Thank you for using this service!')
        logging.info('\nThe employee session has concluded.\n')

    db_handler.update_csv(db)
    logging.info('\nDatabase file has been updated successfully.\n')

if __name__ == '__main__':
    main()