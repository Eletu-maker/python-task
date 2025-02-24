import unittest
from datetime import datetime
import expense_tracker

class Test_the_function(unittest.TestCase):
	def test_expense(self):
		data={"date": "2024-02-24",
            "description": "lunch",
            "amount": 15.75
}
		self.assertEqual(expense_tracker.add_expense(), data)

	def test_expenses(self):
		output =[{"date": "2024-02-24","description": "lunch","amount": 15.75},{"date": "2024-02-24","description": "dinner","amount": 10.75},{"date": "2024-02-24","description": "breakfast","amount": 25.00}]
		self.assertEqual(expense_tracker.expense_tracker(), output)


if __name__ =="__main__":
	unittest.main()