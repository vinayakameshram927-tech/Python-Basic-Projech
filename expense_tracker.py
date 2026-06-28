expenses = []
print("=== Personal Expense Tracker ===")
m_budget = int(input("Enter Your monthly budget: "))

def add_expense():
        desc = input("Enter Description: ")
        cata = input("Enter Catagory: ") 
        date = input("Enter Date (DD-MM-YYYY): ")
        
        try:
            amt = float(input("Enter Amount: "))
            if amt <= 0:
                print("Entered amount is zero or less than 0")
                print("Re-enter the value")
                return
        
        except ValueError:
            print("Amount should be greater than 0 !!")
            return
        
        exp_dict = {
                        "description":desc,
                        "catagory":cata,
                        "amount":amt,
                        "date":date
                    }
        expenses.append(exp_dict)
        
def view_expenses():
    for i in expenses:
        print("| Description: ",i["description"],"| Catagory: ",i["catagory"],"| Amount: ",i["amount"],"| Date: ",i["date"])
        
def category_summary():
    food = 0
    shopping = 0
    for i in expenses:
        if i["catagory"].lower() == "food":
            food = food + i["amount"]
            
        elif i["catagory"].lower() == "shopping":
            shopping = shopping + i["amount"]
            
    print("Food: ",food)
    print("Shopping: ",shopping)
    
def get_top_category():
    food = 0
    shopping = 0
    for i in expenses:
        if i["catagory"].lower() == "food":
            food = food + i["amount"]
            
        elif i["catagory"].lower() == "shopping":
            shopping = shopping + i["amount"]
            
    if food > shopping:
        print("Top Catagory: Food rs.",food)
    else:
        print("Top Catagory: Shopping rs.",shopping)
        
def budget_report():
    total = 0
    for i in expenses:
        total = total + i["amount"]
        
    remain = m_budget - total
    used = (total/m_budget)*100
    print("Total Spent    : ",total)
    print("Monthly Budget : ",m_budget)
    print("Remaining      : ",remain)
    print("Used           : ",round(used,2))
    
    if used > 80:
        print("Warning!! , You have used",round(used,2),"% of your Budget. ")
        get_top_category()
        
while(True):
    print("1. Add       2. View     3. Catagory     4. Report       5. Exit")
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        print("_______________________")
        add_expense()
        print("_______________________")
    
    elif choice == 2:
        print("_______________________")
        view_expenses()
        print("_______________________")
        
    elif choice == 3:
        print("_______________________")
        category_summary()
        print("_______________________")
        
    elif choice == 4:
        print("_______________________")
        budget_report()
        print("_______________________")
        
    elif choice == 5:
        print("Thats all about Your Expense !!")
        break
    else:
        print("Incorrect Choice")
        print("Re-enter the choice")
        
     