import unittest
import to_do_list

class Test_the_function(unittest.TestCase):
	def test_option(self):
		data = "1"
		self.assertEqual(to_do_list.print_to_DO_list(), data)
	def test_option(self):
		data = "2"
		self.assertEqual(to_do_list.print_to_DO_list(), data)





if __name__ =="__main__":
	unittest.main()