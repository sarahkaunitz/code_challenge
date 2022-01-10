import sys
import pandas as pd

# Check if the correct version of Python is loaded... if not, exit
if sys.version[0] != '3':
    print('This script requires Python version: Python3')
    sys.exit(1)

from functions import (get_fraud_file,
                        load_transaction_files, 
                        get_prefix_column,
                        filter_transactions,
                        filter_fraud_in_transactions,
                        get_fraud_by_state,
                        get_fraud_by_vendor,
                        mask_credit_cards)

test_fraud_file1 = ('test_datasets/test_fraud')
test_file_list = ['test_datasets/transaction_test1','test_datasets/transaction_test2']
credit_cards = ['5018','5020','2131','56','300', '6011']


def test_get_fraud_file():
    """
    Testing if the get_fraud_file function
    works as expected. 
    Tests Include: 
    - if the length of the data is as expected; should be 5
    """
    fraud_dataset1 = get_fraud_file(test_fraud_file1)
    assert len(fraud_dataset1) == 5

def test1_load_transaction_files():
    transaction_files = load_transaction_files(test_file_list)
    assert type(transaction_files) == pd.core.frame.DataFrame
 
def test2_load_transaction_files():
    transaction_files = load_transaction_files(test_file_list) 
    assert len(transaction_files) == 10

def test1_get_prefix_column():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    assert start_vals == [5018,5020,2131,56,300,6011,2131]

def test2_get_prefix_column():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    assert all(start_vals)

def test1_filter_transactions():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    assert type(numbers) == pd.core.series.Series
 
def test2_filter_transactions():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    assert len(valid_results) == 7

def test3_filter_transactions():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    assert valid_results['start_val'][0] == 5018

def test4_filter_transactions():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    for i in range(len(fraud_results)):
        assert fraud_results['valid_vendor'][i] == False
 
def test5_filter_transactions():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    for i in range(len(valid_results)):
        assert valid_results['valid_vendor'][i] == True

def test1_filter_fraud_in_transactions():
    fraud_dataset1 = get_fraud_file(test_fraud_file1)
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset1, valid_results)
    assert len(valid_transactions) == 6

def test2_filter_fraud_in_transactions():
    fraud_dataset1 = get_fraud_file(test_fraud_file1)
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset1, valid_results)
    assert '5018192281' in fraud_transactions['credit_card_number'][0]

def test_get_fraud_by_state():
    fraud_dataset1 = get_fraud_file(test_fraud_file1)
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset1, valid_results)
    fraud_by_state = get_fraud_by_state(fraud_transactions)
    assert fraud_by_state.index[0] == 'AZ'
    
def test_get_fraud_by_vendor():
    fraud_dataset1 = get_fraud_file(test_fraud_file1)
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset1, valid_results)
    fraud_transactions, fraud_by_vendor = get_fraud_by_vendor(fraud_transactions)
    assert len(fraud_transactions) == 1

def test_mask_credit_cards():
    transaction_files = load_transaction_files(test_file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    final_df  = mask_credit_cards(valid_results)
    assert final_df['credit_card_number'][0] == '5*********'


