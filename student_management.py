details = {}        # Declared Empty Dictionary

def Add():  # Function to add new student Entry
    name = input("Enter Your name: ")
    roll = int(input("Enter Your roll number: "))
    marks = 0
    print("Enter marks of 5 subjects:")
    for i in range(5):
        n = int(input())
        marks += n
    per = marks/5
    grade = ""
    if per >= 85:
        grade = "A"
    elif per >= 65:
        grade = "B"
    elif per >= 55: 
        grade = "c"
    elif per >=40:
        grade = "D"
    else:
        grade = "Fail"
    details.update({roll:{"name":name,"marks":per,"grade":grade}})
    

def View(): # Function to view all students details
    print("Name \tRollNo \tMarks \tGrade")
    for i in details:
        print(details[i]["name"],i,details[i]["marks"],details[i]["grade"],sep =" \t ")
    

def Search():   # Function to search data of particular student
    roll = int(input("Enter Roll No to search data: "))
    if roll in details:
        print("Name: ",details[roll]["name"]," | Roll No: ",roll," | Marks: ",details[roll]["marks"]," | Grade: ",details[roll]["grade"])
        print("<<<  Record Searched  >>>")
    else:
        print("<<<  Record Not found  >>>")


def Update():   # Function to update data of student
    roll = int(input("Enter Roll No to Update data: "))
    if roll in details:
        print("Which Record do you want to Update: ")
        while(True):
            print("1. Name      2. Marks        3. Grade")
            ch = int(input("ENter Your choice: "))
            if ch == 1:
                upname = input("Enter New Name: ")
                details[roll]["name"] = upname
                break
            elif ch == 2:
                upmark = float(input("Enter new marks: "))
                details[roll]["marks"] = upmark
                break
            elif ch == 3:
                upgrade = input("Enter new grade: ")
                details[roll]["grade"] = upgrade
                break
            else:
                print("Invalid choice! Re-enter choice ")
        print("<<<  Record Updated  >>>")
    else:
            print("<<<  Record Not found  >>>")
            
def Delete():   # Function to delete the data of student
    rn = int(input("Enter Roll number to remove Data: "))
    while(True):
        if rn in details:
            print("1. confirm deletion      2. Cancel ")
            con = int(input("Enter Choice: "))
            if con == 1:
                details.pop(rn)
                print("<<<  Record Removed  >>>")
                break
            else: 
                break
        else:
            print("<<<  Roll no is not in Records  >>>")
            print("--- Please! Add Student First --- ")
            break
        
print("--- Student Management System ---")
# Loop for continuously asking for a choice
while(True):
    print("1. Add Student       2. View all")
    print("3. Search            4. Update")
    print("5. Delete            6. Exit")
    ch = int(input("Enter Choice: "))
    
    if ch == 1:
        print("-------------------------")
        Add()
        print("<<<  Record Added  >>>")
        print("-------------------------")
        
    elif ch == 2:
        print("-------------------------")
        View()
        print("<<<  See all Records above  >>")
        print("-------------------------")
        
    elif ch == 3:
        print("-------------------------")
        Search()
        print("-------------------------")
        
    elif ch == 4:
        print("-------------------------")
        Update()
        print("-------------------------")
        
    elif ch == 5:
        print("-------------------------")
        Delete()
        print("-------------------------")
        
    elif ch == 6:
        print("-------------------------")
        print("Thank You !!")
        print("-------------------------")
        break 
    
    else:
        print("Invalid Choice !! Re-enter Choice ")    
    