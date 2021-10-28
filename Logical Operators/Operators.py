# Looking at AND/OR operators
"""
ex.
if applicant has high income AND good credit
    Eligable for loan
"""
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit: # All conditions must be true for 'and'
    print("Eligable for loan")

"""
ex.
if applicant has high income OR good credit
    Eligable for loan
"""
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit: # At least one condition must be true for 'or'
    print("Eligable for loan")

# the NOT operator
has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record: # 'not' changes the boolean value of the variable
    print("Eligable for loan")
