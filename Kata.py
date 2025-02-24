def main():
    print("=" * 40)
    print(" Welcome to the Multi-Function Program ")
    print("=" * 40)
    print(" - Check even/odd")
    # Check if a number is even or odd
    is_even = int(input("Enter a number: "))
    if is_even % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    print(" - Prime number check")
    # Check if a number is prime
    prime_number = int(input("Enter a prime number: "))
    if prime_number == 0 or prime_number == 1:
        print(f"{prime_number} is not prime.")
    else:
        flag = 0
        for count in range(2, prime_number):
            if prime_number % count == 0:
                print(f"{prime_number} is not prime.")
                flag = 1
                break
        if flag == 0:
            print(f"{prime_number} is prime.")
    print(" - Subtraction")
    # Subtraction of two numbers
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    subtracted_number = first_number - second_number
    print(f"Answer is {abs(subtracted_number)}")
    print(" - Division")
    # Division of two numbers
    quotient_first_number = int(input("Enter first number: "))
    quotient_second_number = int(input("Enter second number: "))
    if quotient_second_number == 0:
        print("Answer is 0 (division by zero)")
    else:
        quotient = quotient_first_number / quotient_second_number
        print(f"Answer is {quotient}")
    print(" - Factors")
    # Find factors of a number
    factor = int(input("Enter number to get the factors: "))
    print(f"Factors of {factor} are:")
    for divisible in range(factor, 0, -1):
        if factor % divisible == 0:
            print(divisible)
    print(" - Check square root")
    # Check if a number is a perfect square
    square_number = int(input("Enter number to check if it is a square: "))
    square_root = square_number ** 0.5
    if square_root.is_integer():
        print("true")
    else:
        print("false")
    print(" - palindrome")
    # Check if a 5-digit number is a palindrome
    five_digit_number = int(input("Enter a 5-digit number to check for palindrome: "))
    if str(five_digit_number) == str(five_digit_number)[::-1]:
        print(f"{five_digit_number} is a palindrome")
    else:
        print(f"{five_digit_number} is not a palindrome")
    print(" - factorial")
    # Calculate the factorial of a number
    factorial_number = int(input("Enter number to calculate factorial: "))
    factorial_answer = 1
    for i in range(1, factorial_number + 1):
        factorial_answer *= i
    print(f"Factorial of {factorial_number} is {factorial_answer}")
    print(" - Check square ")
    # Calculate the square of a number
    get_the_square = int(input("Enter number to get the square: "))
    squared_digits = get_the_square ** 2
    print(f"{get_the_square} squared is {squared_digits}")


if __name__ == "__main__":
    main()
