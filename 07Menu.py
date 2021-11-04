import os
clearConsole = lambda : os.system("cls")

def main_menu():
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Alicia Rodrigues                     |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("")
    menu_list()
    enter_op = input("Enter an option ")

    while enter_op != "x":
        if enter_op == "1":
            start()
            hello_world()
            end()
            clearConsole()
            main_menu()
        elif enter_op == "2":
            start()
            goodbye_world()
            end()
            clearConsole()
            main_menu()          
        elif enter_op == "3":
            start()
            goodbye_person()
            end()
            clearConsole()
            main_menu() 
        elif enter_op == "4":
            start()
            goodbye_teacher()
            end()
            clearConsole()
            main_menu() 
        elif enter_op == "5":
            start()
            for_loop()
            end()
            clearConsole()
            main_menu() 
        elif enter_op == "6":
            start()
            while_loop()
            end()
            clearConsole()
            main_menu() 
        elif enter_op == "7":
            start()
            string_loop()
            end()
            clearConsole()
            main_menu() 
        elif enter_op == "8":
            start()
            convertto_ascii()
            end()
            clearConsole()
            main_menu() 
        else:
            start()
            print("invalid option")
            end()
            clearConsole()
            main_menu()
    start()
    end()
    quit()

def menu_list():
    print("""1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
5. forLoop
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
x. To Exit""")

def start():
    print("")
    print("----Start of Output ---------------------------")
    print("")

def end():
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")

def hello_world():
    print("Hello World")

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

def string_loop():
    string = input("What is your string? ")
    for a in string:
        print(a)

def convertto_ascii():
    string = input("What is your string? ")
    for a in string:
        x = ord(a)
        print(x)  

clearConsole()
main_menu()







