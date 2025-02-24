print("""
       


       _____________________________________________________
       | Collect Rate    | Amount Per Parcel  | Base Pay   |
       `````````````````````````````````````````````````````
       | Less than 50%   |                 160|      5,000 |
       `````````````````````````````````````````````````````
       | 50 - 59%        |                 200|      5,000 |
       `````````````````````````````````````````````````````
       | 60 - 69%        |                 250|      5,000 |
       `````````````````````````````````````````````````````
       | >= 70%          |                 500|      5,000 |
       `````````````````````````````````````````````````````


""")
try:
	number_of_delivery = int(input("Enter number of delivery: "))


	def payment(number_of_delivery):
		if number_of_delivery == 0:
			print("Rider is unavailable !!!")
		elif number_of_delivery < 50:
			parcel = int(160)
			expectResult = number_of_delivery * parcel + 5000
			print(f"anmount paid is N{expectResult}.")
		elif number_of_delivery < 60:
			parcel = int(200)
			expectResult = number_of_delivery * parcel + 5000
			print(f"anmount paid is N{expectResult}.")
		elif number_of_delivery < 70:
			parcel = int(250)
			expectResult = number_of_delivery * parcel + 5000
			print(f"anmount paid is N{expectResult}.")
		else:
			parcel = int(500)
			expectResult = number_of_delivery * parcel + 5000
			print(f"anmount paid is N{expectResult}.")


	payment(number_of_delivery)
except ValueError:
	print("Invalid value")
