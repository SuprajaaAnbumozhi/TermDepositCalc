def calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid):
    """
    Calculates the final value of the investment using Compound Interest formula.

    Args:
        start_amount (P): The initial deposit amount.
        interest_rate (r): The annual interest rate (decimal).
        investment_term (t): The investment term in years.
        interest_paid (n): The interest paid frequency ("Monthly", "Quarterly", "Annually", or "At Maturity").

    Returns:
        The final balance (rounded to two decimal places) as Bendigo bank calculator rounds to the nearest cent.
    """

    interest_rate_per_period = interest_rate / 100

    if interest_paid == investment_term:
        # compound_factor = (1 + Rt) 
        compound_factor = (1 + interest_rate_per_period * investment_term)
    else:
        # compound_factor = (1 + r/n) ** nt
        compound_factor = (1 + interest_rate_per_period / interest_paid) ** (investment_term * interest_paid)
        
    compound_interest = start_amount * compound_factor

    return round(compound_interest)

def get_valid_start_amount():
    """
    Continuously prompting the user to enter a starting deposit amount until a valid amount 
    ranging between 1,000 and 1,500,000 is inputted.
    The limitation is based on https://www.bendigobank.com.au/calculators/deposit-and-savings/
    """
    while True:
        try:
            start_amount_str = input('Enter the start deposit amount (between 1,000 and 1,500,000): ').replace(',', '')
            start_amount = int(start_amount_str)
            if 1000 <= start_amount <= 1500000:
                return start_amount
            else:
                print('Invalid input. Please enter a value between 1,000 and 1,500,000.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

def get_investment_term_years():
    """
    Continuously prompting the user to enter the total number of years of the investment period.
    """
    while True:
        years = input('Investment term in years: ')
        if not years.isdigit():
            print('Number of years need to be a whole number.')
            continue
        return int(years)
    
def get_investment_term_months():
    """
    Continuously prompting the user to enter the total number of months of the investment period.
    """
    while True:
        months = input('Investment term in months: ')
        if not months.isdigit():
            print('Number of months need to be a whole number.')
            continue
        return int(months)


def get_valid_investment_term():
    """
    Continuously prompting the user to enter the total number of years and months of the investment period 
    until valid months ranging from 3 months to 60 months is inputted and returns the total number of years.
    The limitation is based on https://www.bendigobank.com.au/calculators/deposit-and-savings/
    """
    while True:
        years = get_investment_term_years()
        months = get_investment_term_months()

        total_months = years * 12 + months

        if 3 <= total_months <= 5 * 12:
            return round(total_months / 12, 2)
        else:
            print('The combined term should be between 3 months and 5 years. Enter again.')


def get_valid_interest_paid(investment_term):
    """
    Continuously prompting the user to enter the interest paid until they choose a valid method and returns how
    frequent the term deposit reinvests.
    """
    frequency_mapping = {
                            'Monthly': 12, 
                            'Quarterly': 4, 
                            'Annually': 1, 
                            'At Maturity': investment_term
                        }

    if investment_term < 1:
        # Cannot find "Annually" tab in the Bendigobank calculator for less than a year
        del frequency_mapping['Annually']

    while True:
        print('Choose the interest paid frequency:')
        for i, option in enumerate(frequency_mapping.keys(), start=1):
            print(f'{i}. {option}')

        choice = input('Enter the number corresponding to your choice: ')
        if choice.isdigit() and 1 <= int(choice) <= len(frequency_mapping):
            return frequency_mapping[list(frequency_mapping.keys())[int(choice) - 1]]
        else:
            print('Invalid choice. Please enter a valid number.')

def main():
    """
    Call all the necessary functions to get the inputs 
    initial deposit amount, interest rate, investment term 
    and interest frequency and calls a function to calculate the final balance and displays it.
    """
    start_amount = get_valid_start_amount()
    interest_rate = float(input('Enter the interest rate in percentage: '))
    print("""Enter the investment term in years and months separately (between 3 months to 5 years)
                     For example:
                       - 2 years and 3 months: Enter 2 for years and 3 for months.
                       - 5 months: Enter 0 for years and 5 for months.
                       - 3 years: Enter 3 for years and 0 for months.""")
    investment_term = get_valid_investment_term()
    interest_paid = get_valid_interest_paid(investment_term)

    # Calculate final value of the investment
    final_balance = calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid)

    print("Final balance: ", final_balance)

if __name__ == '__main__':
    main()
