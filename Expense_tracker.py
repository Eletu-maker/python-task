from datetime import datetime

def expense_tracker():
    curr = datetime.now().date()
    
    print("Welcome to semicolon Expense Tracker App")
    print("`" * 40)
    print("""
1. Add an expense
2. View all expense
3. Calculate total expenses
4. Exit
""")
    
    is_valid = True
    expenses = []
    total = 0
    option = input("Enter your choice: ")
    while option not in ["1", "2", "3", "4"]:
        print("invalid response")
        print("")
        option = input("Enter your choice: ")
    
    match option:
        case "1":
            expense = {"date": "", "description": "", "amount": ""}
            expense["date"] = curr
            print(f"Enter the date(YYYY-MM-DD): {curr} ")
            expense["description"] = input("Enter the description: ")
            while expense["description"] == "":
                print("You have to input an item")
                expense["description"] = input("Enter the description: ")

            while is_valid:
                try:
                    expense["amount"] = int(input("Enter the amount: "))
                    is_valid = False
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    print("")
            is_valid = True
            total += expense["amount"]
            expenses.append(expense)
    
        case "2":
            print("No record made yet")
        case "3":
            print("No record made yet")
        case "4":
            print("Bye")
    
    while option in ["1", "2", "3"]:
        print("""
1. Add an expense
2. View all expense
3. Calculate total expenses
4. Exit
""")
        is_valid = True
        option = input("Enter your choice: ")
        while option not in ["1", "2", "3", "4"]:
            print("Invalid response")
            option = input("Enter your choice: ")
    
        match option:
            case "1":
                expense = {"date": "", "description": "", "amount": 0}
                expense["date"] = curr
                print(f"Enter the date(YYYY-MM-DD): {curr} ")
                expense["description"] = input("Enter the description: ")
                while expense["description"] == "":
                    print("You have to input an item")
                    expense["description"] = input("Enter the description: ")
                while is_valid:
                    try:
                        expense["amount"] = int(input("Enter the amount: "))
                        is_valid = False
                    except ValueError:
                        print("Invalid input! Please enter a number.")
                        print("")
                is_valid = True
                total += expense["amount"]
                expenses.append(expense)
    
            case "2":
                if expenses == []:
                    print("No record made yet")
                else:
                    print("Date              Description              Amount")
                    for value in expenses:
                        print(f"{value['date']}          {value['description']}                   {value['amount']}")
            case "3":
                if total == 0:
                    print("No record made yet")
                else:
                    print(f"The total expenses are {total}")
            case "4":
                print("Bye")


expense_tracker()
