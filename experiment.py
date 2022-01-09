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

fraud_file = ('/Users/sarahkaunitz/Documents/deloitte/AI_Engineering_Code_Challenge/datasets/fraud')
def get_fraud_file(file):
    '''
    NEED TO ADD DOCSTRING
    TAKES IN A FILE, PARSES OUT RELEVANT CC INFO
    RETURNS LIST OF CREDIT CARD NUMBERS
    '''
    with open(file) as f:
        # Remember, not every row has a 'state' value
        # Only a few rows do
        # From this file we mainly care about the credit card number
        fraud_data = csv.reader(f)
        for index, row in enumerate(fraud_data):
            if len(row) > 2:
                state = row[2]# row[2] State (not always there)
            else:
                # Insert NULL for state
                state = None
            fraud_dataset = [x[0] for x in fraud_data]
    
    return fraud_dataset
fraud_dataset = get_fraud_file(fraud_file) 