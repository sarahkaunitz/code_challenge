from functions import (get_fraud_file,
                        load_transaction_files,
                        get_prefix_column,
                        filter_transactions,
                        filter_fraud_in_transactions,
                        get_fraud_by_state,
                        get_fraud_by_vendor,
                        mask_credit_cards,
                        make_json_file)
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
    fraud_by_state = get_fraud_by_state(fraud_transactions)
    fraud_transactions, fraud_by_vendor = get_fraud_by_vendor(fraud_transactions)
    final_df = mask_credit_cards(valid_results.head())
    make_json_file(final_df)


if __name__ == "__main__":
    main()


