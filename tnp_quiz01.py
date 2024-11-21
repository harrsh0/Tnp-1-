import getpass
import os
import platform

# Function to clear screen
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Dictionary to store users
users = {}
# Dictionary to store quizzes - you can add your own questions and answers here
quizzes = {
    "Quiz1": {
        'What is the correct way to define a variable in Python?\na) variable = value\nb) value = variable\nc) var: value\nd) define variable = value':'a',
        'Which data type is used to represent a sequence of characters in Python?\na) int\nb) float\nc) str\nd) bool':'c',
        'How do you comment a single line in Python?\na) // This is a comment\nb) # This is a comment\nc) /* This is a comment */\nd) ; This is a comment':'b',
        'Which operator is used for integer division in Python?\na) /\nb) //\nc) %\nd) **':'b',
        'How do you create an if-else statement in Python?\na) if condition: statement1\nb) if condition: statement1 else: statement2\nc) if condition then statement1\nd) if condition { statement1; }':'b',
        'What is the purpose of a while loop in Python?\na) To execute a block of code repeatedly until a condition becomes false.\nb) To execute a block of code a fixed number of times.\nc) To create functions.\nd) To define variables.':'a',
        'How do you define a function in Python?\na) function name(): statements\nb) def name(): statements\nc) create function name(): statements\nd) function name(arguments): statements':'b',
        'What is the purpose of the return statement in a Python function?\na) To define the function name.\nb) To end the function execution.\nc) To return a value from the function.\nd) To take input arguments for the function.':'c',
        'How do you import a module named mymodule in Python?\na) import mymodule\nb) include mymodule\nc) use mymodule\nd) load mymodule':'a',
        'How do you access the first element of a list named my_list in Python?\na) my_list[0]\nb) my_list.first()\nc) my_list(0)\nd) my_list[1]':'a',
        'How do you get input from the user in Python?\na) input()\nb) get_input()\nc) read_input()\nd) input_value()':'a',
        'How do you print a message to the console in Python?\na) print()\nb) display()\nc) show()\nd) output()':'a',
        'What is the purpose of a try-except block in Python?\na) To handle errors that may occur during program execution.\nb) To define functions.\nc) To create loops.\nd) To import modules.':'a',
        'What is the difference between a list and a tuple in Python?\na) Lists are mutable, while tuples are immutable.\nb) Lists are immutable, while tuples are mutable.\nc) Both lists and tuples are mutable.\nd) Both lists and tuples are immutable.':'a',
        'How do you create a set in Python?\na) using curly braces\nb) using square brackets []\nc) using parentheses ()\nd) using the set() function':'a',
        'What is the purpose of a dictionary in Python?\na) To store a sequence of elements.\nb) To store key-value pairs.\nc) To store a set of unique elements.\nd) To define functions.':'b',
        'What is a class in Python?\na) A blueprint for creating objects.\nb) A collection of functions.\nc) A data type.\nd) A variable.':'a',
        'What is a module in Python?\na) A collection of functions and classes.\nb) A data type.\nc) A variable.\nd) An object.':'a',
        'What is a package in Python?\na) A collection of modules.\nb) A data type.\nc) A variable.\nd) An object.':'a',
        'How do you import the math module in Python?\na) import math\nb) include math\nc) use math\nd) load math':'a'
    },
    "Quiz2": {
        'What is the correct syntax to declare a variable in C++?\na) variable = value\nb) value = variable\nc) var: value\nd) datatype variable_name;':'d',
        'Which data type is used to represent whole numbers in C++?\na) int\nb) float\nc) char\nd) string':'a',
        'What is the difference between int and long in C++?\na) int is used for smaller integers, long is used for larger integers\nb) int is used for larger integers, long is used for smaller integers\nc) There is no difference between int and long\nd) int is used for floating-point numbers, long is used for integers':'a',
        'How do you declare a constant variable in C++?\na) const variable_name = value;\nb) variable_name const = value;\nc) constant variable_name = value;\nd) define variable_name = value;':'a',
        'Which operator is used for logical AND in C++?\na) &&\nb) ||\nc) !\nd) ^':'a',
        'How do you increment the value of a variable x by 1 in C++?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
        'How do you create an if-else statement in C++?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
        'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
        'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
        'How do you define a function in C++?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
        'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
        'What is a pointer in C++?\na) A variable that stores the address of another variable\nb) A constant value\nc) A data type\nd) A function':'a',
        'How do you dereference a pointer in C++?\na) Using the * operator\nb) Using the & operator\nc) Using the -> operator\nd) Using the [] operator':'a',
        'How do you declare an array in C++?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
        'What is the index of the first element in a C++ array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
        'How do you access the third element of an array named arr in C++?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
        'What is a string in C++?\na) An array of characters\nb) A data type\nc) A function\nd) A constant value':'a',
        'What is a class in C++?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
        'How do you define a class in C++?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
        'What is an object in C++?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a'
    },
    "Quiz3": {
        'What is the correct syntax to declare a variable in C++?\na) variable = value\nb) value = variable\nc) var: value\nd) datatype variable_name;':'d',
        'Which data type is used to represent whole numbers in C++?\na) int\nb) float\nc) char\nd) string':'a',
        'What is the difference between int and long in C++?\na) int is used for smaller integers, long is used for larger integers\nb) int is used for larger integers, long is used for smaller integers\nc) There is no difference between int and long\nd) int is used for floating-point numbers, long is used for integers':'a',
        'How do you declare a constant variable in C++?\na) const variable_name = value;\nb) variable_name const = value;\nc) constant variable_name = value;\nd) define variable_name = value;':'a',
        'Which operator is used for logical AND in C++?\na) &&\nb) ||\nc) !\nd) ^':'a',
        'How do you increment the value of a variable x by 1 in C++?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
        'How do you create an if-else statement in C++?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
        'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
        'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
        'How do you define a function in C++?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
        'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
        'What is a pointer in C++?\na) A variable that stores the address of another variable\nb) A constant value\nc) A data type\nd) A function':'a',
        'How do you dereference a pointer in C++?\na) Using the * operator\nb) Using the & operator\nc) Using the -> operator\nd) Using the [] operator':'a',
        'How do you declare an array in C++?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
        'What is the index of the first element in a C++ array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
        'How do you access the third element of an array named arr in C++?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
        'What is a string in C++?\na) An array of characters\nb) A data type\nc) A function\nd) A constant value':'a',
        'What is a class in C++?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
        'How do you define a class in C++?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
        'What is an object in C++?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a'
    }
}
# Registration function
def register():
    try:
        username = input("Enter a username: ")
        if username in users:
            clear_screen()
            raise ValueError("Username already exists!")
        password = getpass.getpass("Enter a password: ")
        users[username] = password
        print("Registration successful!")
    except ValueError as ve:
        print(f"Error: {ve}")

# Login function
def login():
    try:
        if not users:
            clear_screen()
            raise ValueError("No users registered. Please register first.")
        username = input("Enter your username: ")
        if username not in users:
            clear_screen()
            raise ValueError("Username not found!")
        password = getpass.getpass("Enter your password: ")
        if users[username] == password:
            print("Login successful!")
            return username
        else:
            clear_screen()
            raise ValueError("Incorrect password!")
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Quiz taking function
def take_quiz(username):
    try:
        print("Choose a quiz type: Quiz1, Quiz2, Quiz3")
        quiz_type = input("Enter quiz type: ")
        if quiz_type not in quizzes:
            clear_screen()
            raise ValueError("Quiz type not found!")

        score = 0
        for question, correct_answer in quizzes[quiz_type].items():
            print(question)
            answer = input("Enter your answer: ")
            if answer == correct_answer:
                score += 1
        print(f"{username}, you scored {score} out of {len(quizzes[quiz_type])}")
    except ValueError as ve:
        print(f"Error: {ve}")

# Main function
def main():
    logged_in_user = None
    while True:
        try:
            print("1. Register")
            print("2. Login")
            print("3. Take Quiz")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register()
            elif choice == '2':
                logged_in_user = login()
            elif choice == '3':
                if logged_in_user:
                    take_quiz(logged_in_user)
                else:
                    clear_screen()
                    print("Please login first.")
            elif choice == '4':
                print("Exiting...")
                break
            else:
                clear_screen()
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()