import unittest
from unittest.mock import patch
from io import StringIO
from term_deposit_calc import get_valid_investment_term, \
    get_investment_term_years, \
    get_investment_term_months, \
    get_valid_interest_paid, \
    get_valid_start_amount, \
    calculate_final_balance, \
    main

class TestTermDepositCalculator(unittest.TestCase):
    def test_valid_input_years_months(self):
        with patch('builtins.input', side_effect=["2", "3"]):
            result = get_valid_investment_term()
            self.assertEqual(result, 2.25)

    def test_valid_input_only_month(self):
        with patch('builtins.input', side_effect=["0", "5"]):
            result = get_valid_investment_term()
            self.assertEqual(result, 0.42)

    def test_valid_input_only_year(self):
        with patch('builtins.input', side_effect=["5", "0"]):
            result = get_valid_investment_term()
            self.assertEqual(result, 5)

    def test_invalid_input_exceeds_limit(self):
        with patch('builtins.input', side_effect=["7", "1", "4", "9"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_valid_investment_term()

        self.assertEqual(result, 4.75)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "The combined term should be between 3 months and 5 years. Enter again."
        )

    def test_valid_input_years(self):
        with unittest.mock.patch('builtins.input', return_value="5"):
            result = get_investment_term_years()
        self.assertEqual(result, 5)

    def test_invalid_input_years(self):
        with patch('builtins.input', side_effect=["abc", "-5", "@", "3"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_investment_term_years()
        self.assertEqual(result, 3)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "\n".join(["Number of years need to be a whole number."] * 3)
        )

    def test_valid_input_months(self):
        with unittest.mock.patch('builtins.input', return_value="5"):
            result = get_investment_term_months()
        self.assertEqual(result, 5)

    def test_invalid_input_months(self):
        with patch('builtins.input', side_effect=["abc", "-5", "@", "3"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_investment_term_months()
        self.assertEqual(result, 3)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "\n".join(["Number of months need to be a whole number."] * 3)
        )
        
    def test_valid_interest_paid(self):
        investment_term = 18
        with patch('builtins.input', return_value="2"):
            result = get_valid_interest_paid(investment_term)

        self.assertEqual(result, 4)
        

    def test_invalid_choice_outrange(self):
        investment_term = 18

        with patch('builtins.input', side_effect=["5", "1"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = get_valid_interest_paid(investment_term)

        self.assertEqual(result, 12)

    def test_valid_start_amt(self):
        with unittest.mock.patch('builtins.input', side_effect=["10000"]):
            result = get_valid_start_amount()
        self.assertEqual(result, 10000)

    def test_valid_start_amt_with_comma(self):
        with unittest.mock.patch('builtins.input', side_effect=["10,000"]):
            result = get_valid_start_amount()
        self.assertEqual(result, 10000)

    def test_invalid_start_amt(self):
        with patch('builtins.input', side_effect=["200", "10000"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_valid_start_amount()
        self.assertEqual(result, 10000)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "Invalid input. Please enter a value between 1,000 and 1,500,000."
        )

    def test_invalid_start_amt_with_spl_char(self):
        with patch('builtins.input', side_effect=["abc", "1405.83", "5000"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_valid_start_amount()
        self.assertEqual(result, 5000)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "\n".join(["Invalid input. Please enter a valid integer."] * 2)
        )

    def test_valid_final_balance_quarterly(self):
        start_amount = 10000
        interest_rate = 1.70
        investment_term = 3
        interest_paid = 4
        result = calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid)
        self.assertEqual(result, 10522)

    def test_valid_final_balance_annually(self):
        start_amount = 15000
        interest_rate = 3
        investment_term = 2.5
        interest_paid = 1
        result = calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid)
        self.assertEqual(result, 16150)

    def test_valid_final_balance_monthly(self):
        start_amount = 1000
        interest_rate = 1.45
        investment_term = 0.5
        interest_paid = 12
        result = calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid)
        self.assertEqual(result, 1007)

    def test_valid_final_balance_maturity(self):
        start_amount = 10000
        interest_rate = 1.10
        investment_term = 3
        interest_paid = 3
        result = calculate_final_balance(start_amount, interest_rate, investment_term, interest_paid)
        self.assertEqual(result, 10330)

    def test_main(self):
        with patch('builtins.input', side_effect=["1000", "1.45", "0", "6", "1"]), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()

        self.assertIn("1007", mock_stdout.getvalue())



if __name__ == '__main__':
    unittest.main()
