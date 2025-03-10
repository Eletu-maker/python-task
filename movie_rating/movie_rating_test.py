import unittest
import movie_rating
from datetime import datetime

class Test_the_function(unittest.TestCase):
	
	def test_option(self):
		self.assertEqual(movie_rating.pick_option(), "1")
		self.assertEqual(movie_rating.pick_option(), "2")
		self.assertEqual(movie_rating.pick_option(), "3")
		self.assertEqual(movie_rating.pick_option(), "4")



	def test_add_movie(self):
		curr = datetime.now().strftime('%Y/%m/%d')
		actual =movie_rating.add_movie()
		result ={"merlin":{
	"Title" : "merlin",
	"Rating" : None,
	"Date" : curr},
				}
		self.assertEqual(actual,result)





	def test_add_rating(self):
		curr = datetime.now().strftime('%Y/%m/%d')
		actual =movie_rating.add_rating()
		result ={"merlin":{
	"Title" : "merlin",
	"Rating" : 5.0,
	"Date" : curr},
				}
		self.assertEqual(actual,result)



	def test_average_rating(self):
		actual =movie_rating.average_rating()
		result = 5.0
		self.assertEqual(actual,result)




	def test_exist_app(self):
		actual =movie_rating.exist_app()
		result = "Goodbye"
		self.assertEqual(actual,result)





if __name__ =="__main__":
	unittest.main()