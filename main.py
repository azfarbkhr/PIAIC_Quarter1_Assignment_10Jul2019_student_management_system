''' 
Assignment Name: Student Management System
prepared by: Syed Azfar Ali
PIAIC
'''

# variables used
p_system_name = "Az Studenent Management System"
p_user_input = 1
p_contact_id = 1



# lists used
l_menu_options = (
    "Add New Student", 
    "Print Students List", 
    "Find Student",
    "Exit"
    )

l_message_codes = {
    "001": {"msg":"You have entered incorrect data.", "type":"Error"},
    "002": {"msg":"The specified option does not exists.", "type":"Error"},
    "003": {"msg":"New student added successfully.", "type":"Success"},
    "004": {"msg":"Student list printed successfully.", "type":"Success"}
}

l_student = {
    "Studen_Name": "",
    "Age": "",
    "Contact_Number": ""
}

l_students = [
    {"name": "Syed Azfar Ali", "age": "26", "contact_number": "0123912381"},
    {"name": "Syed Fashi", "age": "22", "contact_number": "01111111"}
]

# functions used
def f_print_message(p_message_code):
    message = l_message_codes[p_message_code]["msg"]
    message_type = l_message_codes[p_message_code]["type"]
    if message_type == "Error":
        print(message_type + ": " + p_message_code + " - " + message)
    elif message_type == "Success":
        print(message_type + ": " + message)

    input("Press enter to continue...")

######################################




# logic used 
while True:
    try:
        # main menu start printing
        print("==============================")
        print(p_system_name)
        print("Main Menu")
        print("==============================")
        for i in range(len(l_menu_options)):
            print("{option_id}: {option_name}".format(option_id = i, option_name = l_menu_options[i]))
        print("==============================")
        ######################################

        # get user input
        p_user_input = int(input("Select an option to continue: "))
        ######################################

        # check if user input of selected options falls in the listed options 
        if p_user_input < len(l_menu_options):
            
            # user add new student
            print("==============================")
            if l_menu_options[p_user_input] == "Add New Student":
                print(p_system_name + " - " + l_menu_options[p_user_input])
                print("Please enter following student details")
                
                # get contact details
                for i,j in l_student.items():
                    l_student[i] = input("{i}: ".format(i = i))                
                
                # add student details to a list of students
                l_students.append(l_student)

                # get contact id and return message
                p_contact_id = len(l_students) - 1
                print("==============================")
                print("Student ID: " + str(p_contact_id))
                f_print_message("003")
            ######################################

            # user print student list
            elif l_menu_options[p_user_input] == "Print Students List":
                print(p_system_name + " - " + l_menu_options[p_user_input])
                print("ID", end = "\t\t")
                for i in l_student.keys():
                    print(i, end = "\t\t")
                print()
                
                for i in range(len(l_students)):
                    print(str(i), end = "\t\t")
                    for k, v in l_students[i].items():
                        print(v, end ="\t\t")
                    print()
                f_print_message("004")
                print("==============================")
            ######################################

            # user find a student
            elif l_menu_options[p_user_input] == "Find Student":
                print(p_system_name + " - " + l_menu_options[p_user_input])
                print("Press 1 to search students by name.")
                print("Press 2 to search students by student ID.")
                search_by = input("Please select an option to continue: ")
                    

                if search_by == str(1):
                    std_name = input("Student Name: ")
                    for i in range(len(l_students)):
                        if l_students[i]["name"].lower() == std_name.lower():
                            print("student found")
                            
                        pass    

            # user exit the system
            elif l_menu_options[p_user_input] == "Exit":
                print("Thank you for using " + p_system_name)
                print("Good bye")
                print("==============================")
                break
        else:
            f_print_message("002") # if user main menu input falls outside range
    except:
        f_print_message("001") # if some unexpected error occurs