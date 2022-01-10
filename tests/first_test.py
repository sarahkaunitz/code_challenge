import sys
# import pandas as pd
import unittest
# import pytest
from pathlib import Path

# Check if the correct version of Python is loaded... if not, exit
if sys.version[0] != '3':
    print('This script requires Python version: Python3')
    sys.exit(1)

from experiment import (get_fraud_file,
                        load_transaction_files, 
                        get_prefix_column,
                        filter_transactions)


class UnitTestingFunctions(unittest.TestCase):
    def test_get_fraud_file(self):
        """
        Testing if the get_fraud_file function
        works as expected. 
        Tests Include:
        - an 'assertTrue' if the file was loaded properly
        - an 'assertFalse' if no file is provided
        """
        test_fraud_file1 = ('test_datasets/test_fraud')
        fraud_dataset1 = get_fraud_file(test_fraud_file1)
        self.assertTrue(fraud_dataset1)

        test_fraud_file2 = ()
        self.assertFalse(test_fraud_file2)


    def test_load_transaction_file(self):
        """
        Testing if the load_transaction_file function
        works as expected. 
        Tests Include:
        - an 'assertTrue' if the file was loaded properly
        - test if we can load in more than two files 
        - test if we can load in just one file 
        """
        test_file_list = ['test_datasets/transaction_test1','test_datasets/transaction_test2']
        transaction_files = load_transaction_files(test_file_list)
        self.assertTrue(transaction_files)

        test_single_file = ('test_datasets/transaction_test1')
        transaction_file1 = load_transaction_files(test_single_file)
        self.assertTrue(transaction_file1)

        # foo = pd.DataFrame(transaction_files)
        # # This is testing if the dataframe was properly created 
        # pd.testing.assert_frame_equal(transaction_files, foo)
        ## write something for if the files exist
        ## write if the file/path is wrong --> self.assertFalse(df2)

    # def test_get_prefix_column():
    #     """
    #     Testing to see if we can get the prefix_vendor values 
    #     for a valid_vendor credit_card_number 
    #     """
    #     test_file_list = ['test_datasets/transaction_test1','test_datasets/transaction_test2']
    #     transaction_files = load_transaction_files(test_file_list)
    #     start_vals = get_prefix_column(transaction_files)
    #     expected_start_vals = [5018, 5020, 2131, 56, 300, 6011, 2131]
    #     assert start_vals == expected_start_vals
    # #want to add second test if you input new value for [0] if it still works 


    # def test_filter_transactions():
    #     test_file_list = ['test_datasets/transaction_test1','test_datasets/transaction_test2']
    #     transaction_files = load_transaction_files(test_file_list)
    #     start_vals = get_prefix_column(transaction_files)
    #     results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)

if __name__ == '__main__':
    unittest.main()