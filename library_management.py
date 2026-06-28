import datetime
print("___ Library Management System")
master = {
    "9001" : {"title":"Python Programming","author":"ABCD","available":True,"borrower":None,"issue_date":None},
    "9002" : {"title":"Mobile appplication","author":"MNOP","available":True,"borrower":None,"issue_date":None},
    "9003" : {"title":"Java Programming","author":"DCBA","available":True,"borrower":None,"issue_date":None},
    "9004" : {"title":"Flutter Developement","author":"WXYZ","available":True,"borrower":None,"issue_date":None},
    "9005" : {"title":"Artificial Intelligence","author":"JKLM","available":True,"borrower":None,"issue_date":None}
}
def add_book():
    isbn = input("Enter ISBN number (4 digit): ")
    title = input("Enter Title of Book: ")
    name = input("Enter Author name: ")
    master.update({isbn : {"title":title,"author":name,"available":True,"borrower":None,"issue_date":None}})
    print("---  Book Added  ---")

def issue_book():
    ser = input("Enter ISBN number: ")
    if ser in master:
        if master[ser]["available"] == True:
            master[ser]["available"] = False
            b_id = input("Enter Your Id (6 Digit): ")
            d = datetime.date.today()
            master[ser]["borrower"] = b_id
            master[ser]["issue_date"] = d
            print("---  Book Issued  ---")
        else:
            print("Book is already issue to someone else.")
def return_book():
    ser = input("Enter ISBN Number: ")
    if ser in master:
        if master[ser]["available"] == False:
            master[ser]["available"] = True
            master[ser]["borrower"] = None
            master[ser]["issue_date"] = None
        else:
            print("Book in not Borrowed. ")
    print("---  Book Returned  ---")
    
def search_book():
    print("Choose How to search")
    print("1. By Title       2. By Author")
    cho = int(input("Enter your choice: "))
    if cho == 1:
        name = input("Enter Title name: ")
        flag = 0
        for i in master:
            if (master[i]["title"].upper()) == name.upper():
                print("=======================")
                print("ISBN: ",i,"Title: ",master[i]["title"],"\t| Author: ",master[i]["author"],"\t| Availability: ",master[i]["available"]  ,"\t| Borrower: ",master[i]["borrower"]   ,"\t| Issue Date: ",master[i]["issue_date"])
                flag = 1
        if flag == 0:
                print("---  Book not available  ---")
    
    elif cho == 2:
        name = input("Enter Author name: ")
        flag = 0
        for i in master:
            if master[i]["author"].upper() == name.upper():
                print("=======================")
                print("ISBN: ",i,"Title: ",master[i]["title"],"| Author: ",master[i]["author"],"| Availability: ",master[i]["available"],"| Borrower: ",master[i]["borrower"],"| Issue Date: ",master[i]["issue_date"])
                flag = 1
        if flag == 0:
                print("---  Book not available  ---")

def view_catalog():
    print("ISBN\t\tTitle\t\t\t\tAuthor\t\tAvailable\tBorrower\tIssue_date")
    for i in master:
        print(i,master[i]["title"],master[i]["author"],master[i]["available"],master[i]["borrower"],master[i]["issue_date"],sep="\t\t")

def check_due_date():
    ch = input("Enter ISBN number: ")
    if ch in master:
        if master[ch]["issue_date"] != None:
            date = master[ch]["issue_date"]
            i_date = date + datetime.timedelta(days=7)
            print("Issued Date: ",date)
            print("Return date: ",i_date)
        else:
            print("---  Not Borrowed by anyone  ---")
    
    else:
        print("---  Book not present in library  ---")
        
while(True):
    print("------------------------")
    print("1. Add Book          2. Issue Book")
    print("3. Return Book       4. Search Book")
    print("5. View all          6. Check Due date")
    print("7. Exit")
    print("------------------------")
    ch = int(input("Enter Choice: "))
    
    if ch == 1:
        print("=======================")
        add_book()
        print("=======================")
    elif ch == 2:
        print("=======================")
        view_catalog()
        print("=======================")
        print("Choose Book: ")
        issue_book()
        print("=======================")
    elif ch == 3:
        print("=======================")
        return_book()
        print("=======================")
    elif ch == 4:
        print("=======================")
        search_book()
        print("=======================")
    elif ch == 5:
        print("=======================")
        view_catalog()
        print("=======================")
    elif ch == 6:
        print("=======================")
        check_due_date()
        print("=======================")
    elif ch == 7:
        print("=======================")
        print("Thank you!!")
        print("=======================")
        break
    else:
        print("=======================")
        print("Incorrect choice !! Re-enter the Choice ")
        print("=======================")