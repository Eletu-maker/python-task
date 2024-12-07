x =2 
y = 3
print('x =', x)
print('value of', x, '+', x , 'is', (x + x))
print('x =')
print((x + y), '=',(y+x))

print("2. ")

grade = 91

if grade >= 90:
	print('3. congratulations! your', grade,'earn you an A in this course')
print("question 4")
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)



print("5. circle")
radius=2
pi = 3.14159
diameter = 2*radius
circumference = 2 * pi * radius
area = pi*(radius**2)

print(diameter)
print(circumference)
print(area)
print(4%2)

print("question 6")
users_input = int(input("Enter any number: "))

if (users_input % 2 == 0):
	print("The number you have entered is an even number.")

else:
	print("The number you have entered is an odd number.")
print("question 7")
if 1024 % 4 ==0:
	print("1024 is a multiple of 4.")

else:
	print("1024 is not a multiple of 4.")
	
if 2 % 10 ==0:
	print("2 is a multiple of 10.")

else:
	print("2 is not a multiple of 10.")
print("question 8")
print("number  square  cube")
for figute  in range(6):
	
	print(figute,"     ",figute **2,"      ", figute **3)


number1 = int(input("Enter a number one: "))
number2 = int(input("Enter a number two: "))
number3 = int(input("Enter a number three: "))

sum = number1 + number2 + number3
average = sum/3
product = number1 * number2 * number3

print("sum =",sum)
print("average =", average)
print("product =", product)

if number1 > number2 or number1 > number3:
	print(number1," is the largest")
elif number2 > number1 or number2 > number3:
	print(number2," is the largest")
else:
	print(number3," is the largest")
if number1 < number2 or number1 < number3:
	print(number1," is the smallest")
elif number2 < number1 or number2 < number3:
	print(number2," is the smallest")
else:
	print(number3," is the smallest")
	