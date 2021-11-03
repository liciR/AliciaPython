print(" ------------------------------------------------")
print("|                                                |")
print("|    07Menu                                      |")
print("|    Name : Alicia Rodrigues                     |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")

def menu():
    print("""
    1. Hello World
    2. Goodbye World
    3. Goodbye Person
    4. Good Teacher
    5. forLoop
    6. whileLoop
    7. string Loop
    8. Convert to ascii
    9. Encode a string
    x. To Exit""")
    enter_op = input("Enter an option ")

def start():
    print("----Start of Output ---------------------------")

def end():
    print("----End of Output -----------------------------")

def hello_world():
    print("\nHello World\n")

def goodbye_world():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbye_person():
    print('Hello')
    name = input('What is your name ? ')
    print('Goodbye ' + name)

def goodbye_teacher():
    TeacherName = input("Teacher's name (try Mr Horan) ")
    if TeacherName == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(TeacherName + " is an okay teacher") 

def for_loop():
    for x in range(1, 500):
        print(x)

def while_loop():
    subject = input("What is the name of this subject ")
    a = "IST"
    while subject != a:
        print("Not Correct - try again")
        subject = input("What is the name of this subject ")
    else:
        print("")
        print("")
        print(" Congratulations!!")
        print("")
        print("")
        print("")

menu()




