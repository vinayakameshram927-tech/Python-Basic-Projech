questions = [
    ("Which function is used to display output in Python?",
     "A. input()", "B. print()", "C. display()", "D. show()", "B"),

    ("Which function is used to take input from the user?",
     "A. print()", "B. scan()", "C. input()", "D. get()", "C"),

    ("Which symbol is used for comments in Python?",
     "A. //", "B. #", "C. /*", "D. %", "B"),

    ("What is the data type of 'Hello'?",
     "A. int", "B. float", "C. string", "D. list", "C"),

    ("Which of the following is a valid variable name?",
     "A. 1num", "B. num-1", "C. num_1", "D. class", "C"),

    ("What is the output of print(5 + 2)?",
     "A. 52", "B. 7", "C. 3", "D. Error", "B"),

    ("Which data type is used to store whole numbers?",
     "A. int", "B. float", "C. str", "D. bool", "A"),

    ("What is the output of len('Python')?",
     "A. 5", "B. 6", "C. 7", "D. Error", "B"),

    ("Which keyword is used to define a function?",
     "A. function", "B. define", "C. def", "D. fun", "C"),

    ("What is the output of print(type(10))?",
     "A. <class 'int'>", "B. <class 'str'>", "C. <class 'float'>", "D. Error", "A")
]
score = 0
wrong_answers = []

print("----  Quiz Compitition  ----")

def get_answer():
    return input("Enter Answer (A/B/C/D): ").upper()

def evaluate_quiz():
    global score

    qno = 1

    for q in questions:
        print("\nQ.", qno, q[0])
        print(q[1])
        print(q[2])
        print(q[3])
        print(q[4])

        ans = get_answer()

        if ans == q[5]:
            score += 1
        else:
            wrong_answers.append((q[0], q[5]))

        qno += 1

def calculate_grade():
    percent = (score / len(questions)) * 100

    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 40:
        return "C"
    else:
        return "F"

def show_report():
    percent = (score / len(questions)) * 100
    print("________________________")
    print("\nName :", studname)
    print("Roll :", studroll)
    print("Score :", score, "/", len(questions))
    print("Percent :", percent)
    print("Grade :", calculate_grade())
    print("________________________")

def show_wrong_answers():
    print("\nWrong Answers:")
    for q, ans in wrong_answers:
        print("________________________")
        print(q)
        print("Correct Answer:", ans)
        print("________________________")

studname = input("Enter Name: ")
studroll = int(input("Enter Roll No: "))

print("________________________")

evaluate_quiz()
show_report()
show_wrong_answers()
print("________________________")