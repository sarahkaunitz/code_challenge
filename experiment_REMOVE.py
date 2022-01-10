import csv 
import json
import os 
import pandas as pd 
import sys 
from itertools import chain

# prefix_vendor = list of credit first digits that are representing this vendor.
maestro = ['5018', '5020', '5038', '56']
mastercard = ['51', '52', '54', '55', '222']
visa = ['4']
amex = ['34', '37']
discover = ['6011', '65']
diners = ['300', '301', '304', '305', '36', '38']
jcb16 = ['35']
jcb15 = ['2131', '1800']

# Make dictionary of vendors 
vendors = {'maestro' : maestro,
           'mastercard' : mastercard,
           'visa' : visa,
           'amex' : amex,
           'discover' : discover,
           'diners' : diners,
           'jcb16' : jcb16,
           'jcb15' : jcb15}

# Map all credit first digits to the vendor to a flattened list 
credit_cards = maestro + mastercard + visa + amex + discover + diners + jcb16 + jcb15

fraud_file = ('datasets/fraud')
def get_fraud_file(file):
    '''
    Returns a list of all the credit card numbers 
    in the form of stringsfrom the first column 
    of the provided file 

    :param file: a path to the desired csv file
    :rtype: list of strings 
    :return: credit_card_numbers from the file provided
    '''
    with open(file) as f:
        # Acts as a test for checking if the file provided is a valid file and that is it properly accessible. 
        if os.path.isfile(file) and os.access(file, os.R_OK):
            pass
        else:
            print("The fraud file is either missing or not readable")
        fraud_data = csv.reader(f)
        for index, row in enumerate(fraud_data):
            if len(row) > 2:
                state = row[2]# The State column is not always there
            else:
                # Insert NULL for state
                state = None
            # Regarding this dataset, only care about the 'credit_card_number" column
            fraud_dataset = [x[0] for x in fraud_data]
    return fraud_dataset

fraud_dataset = get_fraud_file(fraud_file)


## Part I 
# Sanitize data of both transaction-001.zip and transaction-002.zip by removing transactions where column `credit_card_number` 
# is not part of the previous provided list. For example, a credit card that starts with `98` is not a valid card and should be 
# discarded from the sanitized dataset.

file_list=['datasets/transaction-001','datasets/transaction-002']
def load_transaction_files(file_list):
    '''
    Returns a pandas DataFrame of the provided files

    :param file: a list of files that need to be read-in and loaded
    :rtype: pandas.core.frame.DataFrame
    :return: the complete DataFrame of consisting of the two 
    transaction files provided. The columns are 'credit_card_number',
    'ipv4', 'state'. 
    '''
    for i in range(1,len(file_list)):
    # Acts as a test for checking if the files provided are valid files and that they are properly accessible. 
        if os.path.isfile(file_list[i]) and os.access(file_list[i], os.R_OK):
            pass
        else:
            print("The transaction files are either missing or not readable")
    # Set the first file as the main dataframe 
    main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
    # Grab the second dataframe and concatenate it to the main dataframe 
    for i in range(1,len(file_list)):
        data = pd.read_csv(file_list[i])
        df = pd.DataFrame(data)
        main_dataframe = pd.concat([main_dataframe,df],axis=0)
    # Want to make sure that the indices are listed properly after concatenating the two data frames 
    transaction_files = main_dataframe.reset_index(drop=True)
    return transaction_files

transaction_files = load_transaction_files(file_list)


def get_prefix_column(transaction_files, credit_cards):
    """
    Purpose is to filter the credit card numbers that 
    that start with one of the prefix_vendor numbers 
    provided. Output list is a subset of all 
    500,000 original transaction instances 

    :param transaction_files: pd dataframe of all the 
    transactions given 
    :rtype: list of integers 
    :return: a list of all the prefix vendor values 
    provided for each of the valid credit card number 
    instances. 
    """
    numbers = transaction_files['credit_card_number']
    start_nums = []
    for index, number in enumerate(numbers):
        str_num = str(number)
        strt_val = list(filter(str_num.startswith, credit_cards)) 
        start_nums.append(strt_val)
    start_vals = list(chain(*start_nums)) 
    start_vals = [int(i) for i in start_vals]
    return start_vals

start_vals = get_prefix_column(transaction_files, credit_cards)


def filter_transactions(transaction_files, credit_cards, start_vals):
    """
    Takes in the entire list of transactions, a list of credit card numbers,
    and all of the prefix card numbers for the cards that match a vendor 
    and filters the input dataframe to sanitize the data of the transactions
    where 'credit_card_number' is not part of the credit card list/ 

    :param transaction_files: pd dataframe of all the transactions given 
    :param credit_cards: list of unique prefix numbers for each vendor (str)
    :param start vals: list of the prefix number for each credit card number
    instance that is associated with a valid vendor (int)
    :rtype: pandas.core.frame.DataFrame
    :rtype: pandas.core.series.Series
    :rtype: pandas.core.frame.DataFrame
    :rtype: pandas.core.frame.DataFrame
    :return: dataframe with all 500,000 transactions, with valid_vendor 
    column attached based on if the card number started with one of the 
    prefix values 
    :return: the credit_card_number of all 500,000 transactions 
    :return: a sanitized dataframe with a subset of all transactions, 
    including the prefix value as a column 
    :return: dataframe of the transactions that match up with a 
    credit_card_number listed in the fraud data provided 
    """
    numbers = transaction_files["credit_card_number"]
    str_nums = []
    valid_nums = []
    for index, number in enumerate(numbers):
        str_num = str(number)
        result = list(filter(str_num.startswith, credit_cards)) != [] # if the element startswith a credit_cardscredit_card_numbers value keep it, otherwise, remove 
        valid_nums.append(result) # this a boolean list of 'True' or 'False' if the card matches the valid vendor numbers 
        str_nums.append(str_num) # This is a list of all the transaction values as strings 
    results = pd.DataFrame({'credit_card_number':str_nums,
                            'ipv4':transaction_files['ipv4'],
                            'state':transaction_files['state'],
                            'valid_vendor':valid_nums})
    valid_results = results[results['valid_vendor'] == True]
    valid_results = valid_results.assign(start_val = start_vals)    
    valid_results = valid_results.reset_index(drop=True)
    
    fraud_results = results[results['valid_vendor'] == False]
    fraud_results = fraud_results.reset_index(drop=True)
    return results, numbers, valid_results, fraud_results

results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)


## Part II 
# Find in the sanitized dataset if it contains fraudulent transactions (using the data from loading fraud.zip) and report 
# their number.

def filter_fraud_in_transactions(fraud_dataset, valid_results):
    """
    From the santitized results dataframe 
    filter the DF to display only the numbers
    that are present in the fraud.zip file 
    """
    fraud_transactions = valid_results[valid_results['credit_card_number'].isin(fraud_dataset)].drop_duplicates()
    fraud_transactions = fraud_transactions.reset_index(drop=True)
    fraud_transactions['valid_card'] = False
    valid_transactions = valid_results.drop(fraud_transactions.index)
    valid_transactions['valid_card'] = True
    return valid_transactions, fraud_transactions

valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset, valid_results)

print('Within the sanitized dataframe, there were', len(fraud_transactions), 'instances of fraudulent transactions.')


# - Create a report of the number of fraudulent transactions per state.
def get_fraud_by_state(fraud_transactions):
    """
    Takes in a dataframe (fraud_transactions within valid_results)
    performs a group by on state,
    and returns a json serialized list of the count of
    transactions by state as objects
    """
    fraud_groupby_state = fraud_transactions.groupby('state').count()
    fraud_by_state = fraud_groupby_state[['credit_card_number']]
    fraud_by_state = fraud_by_state.rename(columns={'credit_card_number': 'count'})
    return fraud_by_state

fraud_by_state = get_fraud_by_state(fraud_transactions)


# - Create a report of the number of fraudulent transactions per card vendor, e.g., maestro => 45, amex => 78, etc...
def get_vendors_val_key(item):
    for key, val in vendors.items():
        if item in val:
            return key


def get_fraud_by_vendor(fraud_transactions):
    """
    Takes in an dataframe performs a group by on state,
    and returns a json serialized list of the count of
    transactions by state as objects
    """
    fraud_transactions['start_val']= fraud_transactions['start_val'].map(str)
    fraud_transactions['name'] = fraud_transactions.start_val.map(get_vendors_val_key)
    fraud_groupby_vendor = fraud_transactions.groupby('name').count()
    fraud_by_vendor = fraud_groupby_vendor[['credit_card_number']]
    fraud_by_vendor = fraud_by_vendor.rename(columns={'credit_card_number': 'count'})
    return fraud_transactions, fraud_by_vendor

fraud_transactions, fraud_by_vendor = get_fraud_by_vendor(fraud_transactions)
print(fraud_by_vendor.sum())


# - Create a dataset of 3 columns and save in both JSON and in a binary fileformat that you believe it's suitable for BI analysis:
####   - column 1: masked credit card: replace 9 last digits of the credit card with `*`
####   - column 2: ip address
####   - column 3: state
####   - column 4: sum of number of byte of (column 1 + column 2 + column 3)

def mask_credit_cards(valid_results):
    dicts = []
    for index, row in enumerate(valid_results['credit_card_number']):
        full_card_number = valid_results['credit_card_number'].astype(str).iloc[index][:-9]
        masked = full_card_number + '*' * 9
        ipv4_value = valid_results['ipv4'][index]
        state_value = valid_results['state'][index]
        byte_number = sys.getsizeof(masked + ipv4_value + state_value)
        dict = {'credit_card_number' : masked,
                 'ipv4' : ipv4_value,
                 'state' : state_value,
                 'bytes' : byte_number}
        dicts.append(dict)
    df_dicts = pd.DataFrame(dicts) 
    return df_dicts
# final_df = masked_credit_cards(valid_results)
final_df = mask_credit_cards(valid_results.head())
print(final_df)


def make_json_file(final_df):
    directory = 'results/'
    sample = final_df.to_dict()
    with open(directory + "final_df.json", "w") as outfile:
        json.dump(sample, outfile)
