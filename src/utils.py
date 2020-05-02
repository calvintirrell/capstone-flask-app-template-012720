def validate_input(data):
    test_value = []
    errors = []
    
    EXPECTED_FEATURES = ('Gender', 'Age', 'Debt', 'Married', 'BankClient', 'SchoolLevel',
                         'Ethnicity', 'YearsWorked', 'PriorDefault', 'Employed', 'CreditScore',
                         'Citizen', 'Income', 'Approval')
    
    if not data:
        errors.append("Form data must not be empty")
    else:
        for feature in EXPECTED_FEATURES:
            if feature not in data:
                errors.append(f"'{feature}' is a required field")
            else:
                try:
                    test_value.append(float(data[feature]))
                except ValueError:
                    errors.append(f"Invalid value for field {feature}: '{data[feature]}'")

    return test_value, errors

def get_features(selection):

    # do stuff here
    # use string 'user_1' to retrieve features
    # return inputs
    return [0]