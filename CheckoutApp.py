from typing import List
from datetime import datetime
import math
curr = datetime.now()

print(curr)
item = []
quantity = []
price = []
total = []


sumTotal = 0
name = input("what is the customer,s name? ")
repeat = "yes"
number = 0

while repeat == "yes":
	userbuy = input("what did the user buy? " )
	item.append(userbuy)
	piece = int(input("how many pieces? " ))
	while piece <= 0:
		print("unacceptable value")
		piece = int(input("how many pieces? " ))
	quantity.append(piece)
	howMuch = float(input("how much per unit? " ))
	while howMuch <= 0:
		print("unacceptable value")
		howMuch = int(input("how much per unit? " ))
	price.append(howMuch)
	totalPrice = piece * howMuch
	total.append(totalPrice)
	sumTotal += totalPrice;
	repeat = input("add more items?" )
	while repeat not in ['yes' , 'no']:
		print("wrong answer: either enter yes or no")
		repeat = input("add more items?" )
	number +=1

cashier = input("what is your cashier name: ")
discount = float(input("how much discount will he get?: "))
VATfull = sumTotal * 0.175
VAT = math.ceil(VATfull * 100)/ 100.0
billTotal = sumTotal - discount + VAT

print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
""")
print(f"Date :  {curr}")
print(f"Cashier :  {cashier}")
print(f"Customer name :  {name}")
print(""" 
===========================================================================
         ITEM           QTY       PRICE         TOTAL(NGN)
---------------------------------------------------------------------------
""")
for value in range(number):
	print(f"         {item[value]}           {quantity[value]}        {price[value]}         {total[value]}")

print("-"*75)
print(f"""                      
                           Sub Total:      {sumTotal}
                            Discount:      {discount}
                         VAT @ 17.5%:      {VAT}
                          Bill Total:      {billTotal}
""")
print("="*75)
print(f"               THIS IS NOT A RECIEPT KINDLY PAY {billTotal}")
print("="*75)
	
amount_paid = float(input("how much did the customer give to you?"))
balance = amount_paid - billTotal
while balance < 0:
	print("insufficient fund, guy are u broke?")
	amount_paid = float(input("how much did the customer give to you?"))
	balance = amount_paid - billTotal

print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
""")
print(f"Date :  {curr}")
print(f"Cashier :  {cashier}")
print(f"Customer name :  {name}")
print(""" 
===========================================================================
         ITEM           QTY       PRICE         TOTAL(NGN)
---------------------------------------------------------------------------
""")
for value in range(number):
	print(f"         {item[value]}           {quantity[value]}        {price[value]}         {total[value]}")

print("-"*75)
print(f"""       
                           Sub Total:      {sumTotal}
                            Discount:      {discount}
                         VAT @ 17.5%:      {VAT}
                          Bill Total:      {billTotal}
""")
print("="*75)
print(f"""           
                         Amount Paid:      {amount_paid}
	                     Balance:      {balance}
""")
print("="*75)
print(f"                     THANK YOU")
print("="*75)
