''' 
Assignment Name: Student Management System
prepared by: Syed Azfar Ali
PIAIC
'''

# libraries used
from os import system 


# variables used
p_system_name = "Az Student Management System"
p_user_input = 1
p_student_id = 1



# lists used
l_main_menu_options = (
    "Add New Student", 
    "Print Students List", 
    "Find Student",
    "Exit"
    )

l_search_by_menu = (
    "Search by Student Name",
    "Search by Student ID"
)

l_message_codes = {
    "001": {"msg":"You have entered incorrect data.", "type":"Error"},
    "002": {"msg":"The specified option does not exists.", "type":"Error"},
    "003": {"msg":"New student added successfully.", "type":"Success"},
    "004": {"msg":"Student list printed successfully.", "type":"Success"},
    "005": {"msg":"Student can not be found in the sytem.", "type":"Error"}

}

l_student = {
    "name": "",
    "age": "",
    "student_Number": ""
}

l_students = [
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Fashi", "age": "22", "student_number": "01111111"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"},
    {"name": "Syed", "age": "26", "student_number": "0123912381"}
]

# functions used
#############################
def f_print_message(p_message_code):
    message = l_message_codes[p_message_code]["msg"]
    message_type = l_message_codes[p_message_code]["type"]
    if message_type == "Error":
        print(message_type + ": " + p_message_code + " - " + message)
    elif message_type == "Success":
        print(message_type + ": " + message)

    input("Press enter to continue...")
    system('clear')

#############################
def f_print_screen_headers(p_user_input):
    print(p_system_name + " - " + l_main_menu_options[p_user_input])
    print("="*100)

#############################
def f_add_new_student():
    print("Please enter following student details")
    
    # get student details
    for i,j in l_student.items():
        l_student[i] = input("{i}: ".format(i = i))                
    
    # add student details to a list of students
    l_students.append(l_student)

    # get student id and return message
    p_student_id = len(l_students) - 1
    print("="*100)
    print("Student ID: " + str(p_student_id))
    f_print_message("003")


#############################
def f_print_students_details(p_student_id = -1):
    if p_student_id < 0:
        print("ID", end = "\t\t")
        for i in l_student.keys():
            print(i, end = "\t\t")
        print()
        
        for i in range(len(l_students)):
            print(str(i), end = "\t\t")
            for k, v in l_students[i].items():
                print(v, end ="\t\t")
            print()
        print("="*100)
        f_print_message("004")
        print("="*100)
        return True
    elif p_student_id >= 0:
        if p_student_id > len(l_students):
            f_print_message("005")
            return False
        print("ID", end = "\t\t")
        for i in l_student.keys():
            print(i, end = "\t\t")
        print()
        
        print(p_student_id, end ="\t\t")
        for k, v in l_students[p_student_id].items():
            print(v, end ="\t\t")
        print()
        print("="*100)
        f_print_message("004")
        print("="*100)
        return True
    else:
        f_print_message("005")
        return False

##################################
def f_search_by_student_name(std_name):
    for i in range(len(l_students)):
        if l_students[i]["name"].lower() == std_name.lower():
            print("="*100)
            return(f_print_students_details(i))
    f_print_message("005")
    return False
        



######################################
# logic used 
while True:
    try:
        # main menu start printing
        print(p_system_name + " - Main Menu")
        print("="*100)
        # printing available options using a loop
        for i in range(len(l_main_menu_options)):
            print("{option_id}: {option_name}".format(option_id = i, option_name = l_main_menu_options[i]))
        print("="*100)
        ######################################

        # get user input
        p_user_input = int(input("Select an option to continue: "))
        system('clear')
        ######################################

        # check if user input of selected options falls in the listed options 
        if p_user_input < len(l_main_menu_options):
            
            # user add new student
            print("="*100)
            if l_main_menu_options[p_user_input] == "Add New Student":
                #f_print_screen_headers(p_user_input)
                f_add_new_student()
            ######################################

            # user print student list
            elif l_main_menu_options[p_user_input] == "Print Students List":
                f_print_screen_headers(p_user_input)
                f_print_students_details()
            ######################################

            # user find a student
            elif l_main_menu_options[p_user_input] == "Find Student":
                f_print_screen_headers(p_user_input)
                # print menu option for search by 
                for i in range(len(l_search_by_menu)):
                    print("Press {i} to {j}".format(i = i, j = l_search_by_menu[i]))
                # get user input 
                search_by = int(input("Please select an option to continue: "))

                if l_search_by_menu[search_by] == "Search by Student Name":
                    std_name = input("Student Name: ")
                    f_search_by_student_name(std_name)
                elif l_search_by_menu[search_by] == "Search by Student ID":
                    p_student_id = int(input("Student ID: "))
                    f_print_students_details(p_student_id)

            # user exit the system
            elif l_main_menu_options[p_user_input] == "Exit":
                print("Thank you for using " + p_system_name)
                print("Good bye")
                print("="*100)
                break
        else:
            f_print_message("002") # if user main menu input falls outside range
    except:
        f_print_message("001") # if some unexpected error occurs