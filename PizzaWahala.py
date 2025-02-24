print("""




		                PIZZA WAHALA

            ________________________________________________________
	    | Pizza type     | Number of Slices  | Price per box   |
	    ````````````````````````````````````````````````````````
	    | Sapa size      | 4                 | 2,500           |
	    ````````````````````````````````````````````````````````
	    | Small Money    | 6                 | 2,900           |
	    ````````````````````````````````````````````````````````
	    | Big boy        | 8                 | 4,000           |
	    ````````````````````````````````````````````````````````
	    | Odogwu         | 12                | 5,200           |
	    ```````````````````````````````````````````````````````` 

""")
try:
	guest = int(input("enter number of guest: "))
	print()
	mod = guest % 12
	odogwu = int(guest / 12)
	bigBoy = 0
	smallMoney = 0
	sapaSize = 0
	leftOverSlice = 0;
	totalOfSapaSize = 0;
	totalOfSmallMoney = 0;
	totalOfBigboy = 0;
	totalOfnumberOfPizza = 0;
	totalPrice = 0; 

	if mod >= 8:
		bigBoy += 1 
		leftOverSlice =  mod - 8
	elif mod >= 6:
		smallMoney += 1
		leftOverSlice =  mod - 6
	elif mod >= 4:
		sapaSize += 1
		leftOverSlice =  mod - 4
	

	print(f"Do you want to get  {odogwu} odogwu, {bigBoy} Big boy, {smallMoney} Small money, { sapaSize } Sapa size and still have { leftOverSlice } left over slice.")
	print()


	repeat= True
 
	while repeat:

		orderOption=int(input("If you are interested on our offer enter 1, if you want to order manually enter 2: "))
		print()
		if orderOption == 1 :
			totalOfSapaSize = sapaSize * 2500
			totalOfSmallMoney = smallMoney * 2900
			totalOfBigboy = bigBoy * 4000		
			totalOfnumberOfPizza = odogwu * 5200
			totalPrice = totalOfSapaSize + totalOfSmallMoney + totalOfBigboy  + totalOfnumberOfPizza;
			print(f"your total is: N{totalPrice}")
			repeat= False
		elif orderOption == 2:
			mannualOdogwu =int(input("Enter number of odogwu: "))
			mannualBigboy =int(input("Enter number of Big boy: "))
			mannualSmallmoney =int(input("Enter number of Small money: "))
			mannualSapasize = int(input("Enter number of Sapa size: "))
			mannualTotal = 0;
			priceOfmannualOdogwu = mannualOdogwu * 5200
			priceOfmannualBigboy = mannualBigboy * 4000
			priceOfmannualSmallmoney = mannualSmallmoney * 2900
			priceOfmannualSapasize = mannualSapasize * 2500
			mannualTotal = priceOfmannualOdogwu + priceOfmannualBigboy + priceOfmannualSmallmoney + priceOfmannualSapasize;
			print(f"your total is: N{mannualTotal}")
			repeat= False

		else:
			print("Wrong number !!!")
			print("Try again")
			print()
			repeat = True

except ValueError:
	print("Invalid value")





