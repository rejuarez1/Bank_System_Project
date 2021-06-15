import pandas as pd

def main():
    # try:
    #     db = pd.read_csv('data.csv')
    # except:
    #     db = pd.DataFrame(columns = ['customer_id', 'first_name', 'last_name', 'date_of_birth'])
    #     raise FileNotFoundError("File not found.")
    # finally:
    #     db.to_csv('data.csv')

    cols = ['customer_id', 'employee_id', 'first_name', 'last_name', 'date_of_birth', 'user_name', 'password',
            'checking_acct_id', 'checking_acct_bal', 'savings_acct_id', 'savings_acct_bal',
            'credit_card_id', 'credit_card_limit', 'credit_card_irate', 'credit_card_bal',
            'loan_id', 'loan_limit', 'loan_irate', 'loan_bal']
    db = pd.DataFrame(columns = cols)
    db.loc[-1, ['employee_id']] = 12345
    db.loc[-1, ['first_name']] = 'Rodrigo'
    db.loc[-1, ['user_name']] = 'rejuarez'
    db.loc[-1, ['password']] = 'rj123'

    row = db[db.first_name == 'Rodrigo']
    print(row.customer_id.isna())
    print(row)

    db.to_csv('data.csv')

if __name__ == '__main__':
    main()