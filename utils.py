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