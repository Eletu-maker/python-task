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


	

	
if __name__ =="__main__":
	unittest.main()