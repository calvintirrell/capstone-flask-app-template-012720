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
    # use string "name"" to retrieve inputs to use in model

    if selection == "James_Bond":
        # [...1] = Approved
        jb = [1, 52, 15, 1, 0, 1, 7, 5.5, 1, 1, 14, 0, 2200]

        print(jb)
        return jb

    elif selection == "Hermoine_Granger":
        # [...1] = Approved
        hg = [0, 30, 0.5, 1, 0, 1, 7, 1.75, 1, 1, 11, 0, 540]

        print(hg)
        return hg

    elif selection == "Catwoman":
        # [...0] = Denied
        c = [0, 37, 2.665, 1, 0, 2, 7, 0.165, 0, 0, 0, 0, 501]

        print(c)
        return c

    else:
        # [...0] = Denied
        m = [1, 57, 2, 1, 0, 5, 2, 6.5, 0, 1, 1, 0, 10]

        print(m)
        return m