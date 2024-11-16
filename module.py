def greet(name):
    return "Hello " + name


def teacher_name(class_name):
    if class_name == "Math":
        print("The teacher of this class is Mr. " + "Faiq")
    elif class_name == "English":
        print("The teacher of this class is Mr. " + "John")


def take_input_and_perform_calculation():
    function = input("Enter the function you want to perform: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if function == "add":
        print(add(a, b))

    elif function == "sub":
        print(sub(a, b))

    else:
        print("Invalid function")
