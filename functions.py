#This program will only be used to define the functions    

def list_displayer(input_list):
    print("Welcome to the list replacement game.")
    print("If you feel the need to quit at any time, simply enter QUIT.")
    print("This is your list: ")
    print(input_list)


def users_choice(input_list):
    choice = "Placeholder string"
    while choice.isdigit() == False or int(choice) not in range(len(input_list)):
        print("Choose the index location of the value you want replaced. ")
        choice = input(f"Please enter an index location between 0 and {len(input_list)-1} inclusive: ")
        if choice.lower() == "quit":
            exit()

    return int(choice)


def element_replacer(input_list):
    chosen_index_number = users_choice(input_list)
    replacement = input("Now choose the value you want to be placed in that index location: ")
    if replacement.lower() == "quit":
        exit()
    else:
        replacement = int(replacement)
    input_list[chosen_index_number] = replacement
    print(f"Your list is now {input_list} ")
    continue_playing(input_list)


def continue_playing(input_list):
    decision = "Placeholder string"
    while decision !="Y" or decision != "N":
        decision = input("Would you like to keep playing?[Y/N]: ")
        if decision == "Y":
            element_replacer(input_list)
        elif decision == "N":
            exit()

