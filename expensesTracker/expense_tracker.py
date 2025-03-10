 
def add_expense():
    expense = {"date": "", "description": "", "amount": 0}
    
    date = input("Enter the date (YYYY-MM-DD): ")
    expense["date"] = date
    
    expense["description"] = input("Enter the description: ")
    while expense["description"] == "":
        print("You have to input an item")
        expense["description"] = input("Enter the description: ")
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 1:
                print("No negative numbers or zero allowed.")
            else:
                expense["amount"] = amount
                break
        except ValueError:
            print("Invalid input! Please enter a number.") 
    
    print("Expense added successfully!")
    return expense

def pick_option():
    option = input("Enter your choice: ")
    while option not in ["1", "2", "3", "4"]:
        print("Invalid response")
        option = input("Enter your choice: ")
    return option


def get_total(number):
    if number == 0:
        return "No record made yet"
    else:
        return f"The total expenses are {number}"

def expense_tracker():
    expenses = []
    total = 0
    
    print("Welcome to Semicolon Expense Tracker App")
    print("`"*40)
    while True:
        print("""
1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit
""")
        
        option = pick_option()
        
        match option:
            case "1":
                expense = add_expense()
                total += expense["amount"]
                expenses.append(expense)
            
            case "2":
                if not expenses:
                    print("No record made yet")
                else:
                    print("Date              Description              Amount")
                    for value in expenses:
                        print(f"{value['date']}          {value['description']}                   {value['amount']}")
            
            case "3":
                ans = get_total(total)
                print(ans)
            
            case "4":
                print("Goodbye") 
                
	
                break

expense_tracker()

