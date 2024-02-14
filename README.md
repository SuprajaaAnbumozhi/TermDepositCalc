# Term Deposit Calculator

This Python script (`term_deposit_calc.py`) helps to calculate the potential earnings for a term deposit based on the inputs.

## Description

This script offers the following features:

- Validates user input for start deposit amount and investment term (years and months).
- Handles different interest paid frequencies (monthly, quarterly, annually, at maturity).
- Calculates rounded potential earnings using Compound Interest formula.

## Requirements

- Python 3.x

## How to Use

1. Run `python3 term_deposit_calc.py`.
2. Follow the prompts to enter:
    - Start deposit amount
    - Interest rate in percentage
    - Investment term (years and months)
    - Interest paid frequency
3. The script will display the calculated earnings.

## Testing

- The project includes a separate script (`term_deposit_calc_test.py`) for automated testing. Run the tests using `python3 term_deposit_calc_test.py`.
- Unit tests cover 98% of the code base using the unittest framework.

## Notes

I'm mindful that no specific limitations were outlined. However, based on my understanding of the project in the website provided in the task (https://www.bendigobank.com.au/calculators/deposit-and-savings/), I've tentatively assumed the following limitations might apply: 
- Initial amount between 1,000 - 1,500,000
- Investment term between 3 months - 5 years
