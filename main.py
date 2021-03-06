from functions import (get_fraud_file,
                        load_transaction_files,
                        get_prefix_column,
                        filter_transactions,
                        filter_fraud_in_transactions,
                        get_fraud_by_state,
                        get_fraud_by_vendor, make_binary_file,
                        mask_credit_cards,
                        make_json_file,
                        make_binary_file)
from utils import (vendors, 
                  credit_cards)

def main():
    vendors
    credit_cards
    fraud_file = ('datasets/fraud')
    file_list=['datasets/transaction-001','datasets/transaction-002']

    run(fraud_file, file_list, vendors, credit_cards)

def run(fraud_file, file_list, vendors, credit_cards):
    fraud_dataset = get_fraud_file(fraud_file)
    transaction_files = load_transaction_files(file_list)
    start_vals = get_prefix_column(transaction_files, credit_cards)
    results, numbers, valid_results, fraud_results = filter_transactions(transaction_files, credit_cards, start_vals)
    valid_transactions, fraud_transactions = filter_fraud_in_transactions(fraud_dataset, valid_results)
    print('Within the sanitized dataframe, there were', len(fraud_transactions), 'instances of fraudulent transactions.')
    fraud_by_state = get_fraud_by_state(fraud_transactions)
    print('Report of the number of fraudulent transactions per state')
    print(fraud_by_state)
    fraud_transactions, fraud_by_vendor = get_fraud_by_vendor(fraud_transactions)
    print('Report of the number of fraudulent transactions per card vendor')
    print(fraud_by_vendor)
    final_df = mask_credit_cards(valid_results.head())
    print('Taking a glimpse at the dataset created that contains the masked credit card information')
    print(final_df)
    make_json_file(final_df)
    make_binary_file(final_df)


if __name__ == "__main__":
    main()


