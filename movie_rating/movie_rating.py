from datetime import datetime
def pick_option():
    option = input("Enter your choice: ")
    while option not in ["1", "2", "3", "4"]:
        print("Invalid response")
        option = input("Enter your choice: ")
    return option






def add_movie():
	curr = datetime.now().strftime('%Y/%m/%d')
	global number
	number += 1
	movies_name= input("Enter movie name: ")
	while movies_name == "":
		print("must enter a movie")
		movies_name= input("Enter movie name: ")
	the_movies[movies_name]={
	"Title" : movies_name,
	"Rating" : None,
	"Date" : curr
				}
	return the_movies


def add_rating():
	if number == 0:
		print("no data added")
				
	else:
		for key,value in the_movies.items():
			if value["Rating"] is not None:
				continue
			else:
				while True:
					try:
						value["Rating"]=float(input(f"Enter your rating for {key}: "))
						if value["Rating"]<0 or value["Rating"] >5:
							print("Your rating but be betwwen 0 - 5 ")
							
						else:
							break
						
					except ValueError:
						print("only numbers are allow")
					
	return the_movies

def average_rating():
	if number == 0:
		print("no movie added yet")
	else:
		all_rating=0
		average_rating =0
		for key,value in the_movies.items(): 
			all_rating += value["Rating"]
		average_rating = all_rating/number
	return average_rating

def exist_app():
	global is_repeat
	is_repeat = False
	return "Goodbye"










def option_choice(choice):
	match choice:
		case "1":
			add_movie()					
			
		case "2":
			print(add_rating())
							
		case "3":
			print(f"The average ranting of all the movies  is {average_rating()}")

		case "4":
			print(exist_app())
			
			
		
print("MOVIE RATING SYSTEM")
is_repeat = True
the_movies = dict()
number =0;
while is_repeat:
	print("""
Enter your choice
1. Add a movie 
2. Rate the movie
3. View average rating
4. Exit
""")
	choice = pick_option()
	option_choice(choice)