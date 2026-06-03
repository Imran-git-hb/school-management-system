def heading():
    print("\n\n\n",80*"-","\n\n\n                             SCHOOL MANAGEMENT SYSTEM                              \n\n\n",80*'-',"\n\n\n")

def main_menu():
    print("MAIN MENU")
    print("1. STUDENT SECTION")
    print("2. TEACHER SECTION")
    print("3. OTHERS")
    print("4. EXIT THE PROGRAM")
def student():
    print("\n 1. ADD  STUDENT \n 2. SEARCH STUDENT \n 3. DELETE STUDENT \n 4. UPDATE STUDENT's DETAILS \n 5. DISPLAY ALL DATA \n 6. GO TO PREVIOUS SLIDE \n")
def teacher():
    print("\n 1. ADD TEACHER \n 2. SEARCH TEACHER \n 3. DELETE TEACHER \n 4. UPDATE TEACHER'S DETAILS \n 5. DISPLAY ALL DATA \n 6. GO TO PREVIOUS")
def fee_structure():
    print("\n 1. ADD FEE \n 2. UPDATE FEE DETAILS \n 3. DISPLAY ALL FEE DATA \n 4. GO TO PREVIOUS \n ")
def library_management():
    print("\n 1. ADD BOOK \n 2. REMOVE BOOK \n 3. DISPLAY ALL BOOKS \n 4. GO TO PREVIOUS")

import pickle
import os

#ADD STUDENT
def add_stu():
    ans="Yy"
    while ans in 'Yy':
        rno=int(input("Enter Roll No.:"))
        name=input("Enter Name:")
        cls=int(input("Enter Class:"))
        sec=input("Enter Section:")
        marks=int(input("Enter Total Marks:"))
        perc=float(input("Enter Percentage:"))
        res=input("result (pass or fail): ")
        att=int(input("Attendance:"))
    #Creating Dictionary
        stu={"RollNo":rno,"Name":name,"Class":cls,"Section":sec.upper(),"Total Marks":marks,"Percentage":perc,"Result":res,"Attendance":att}
    #Writing Dictionary to file
        f=open("StudentData.dat","ab")
        pickle.dump(stu,f)
        f.close()
        print("Record Added Successfully.")
        ans=input('Want to enter more records. If YES then Y/y or N/n for NO:')
        

#READ RECORD
def read_stu():
    f=open("StudentData.dat","rb")
    try:
       while True:
            stu=pickle.load(f)
            print("\n")
            print("RollNo:",stu["RollNo"])
            print("Name:",stu["Name"])
            print("Class:",stu["Class"])
            print("Section:",stu["Section"])
            print("Total Marks:",stu["Total Marks"])
            print("Percentage:",stu["Percentage"])
            print("Result:",stu["Result"])
            print("Attendance:",stu["Attendance"])
            print("\n")
    except EOFError:
        print("")
        
            
    f.close()

#SEARCH STUDENT
def search_stu(r_search):
    f=open("StudentData.dat","rb")
    found=False
    try:
        while True:
            stu = pickle.load(f)
            if stu["RollNo"] == r_search:
                print("RollNo:",stu["RollNo"])
                print("Name:",stu["Name"])
                print("Class:",stu["Class"])
                print("Section:",stu["Section"])
                print("Total Marks:",stu["Total Marks"])
                print("Percentage:",stu["Percentage"])
                print("Result:",stu["Result"])
                print("Attendance:",stu["Attendance"])
                found=True
    except EOFError:
            print("")
    if found == False:
        print("No Student Data Found with Roll Number:",r_search)
    f.close()

#UPDATE STUDENT's DETAIL
def update_stu():
    f1 = open("StudentData.dat","rb")
    f2 = open("temp.dat","wb")
    s=int(input("Enter Roll No. to update:"))
    found=0
    while True:
        try:
            stu = pickle.load(f1)
            if stu["RollNo"] == s:
                #NAME
                while True:
                    print('Name:',stu["Name"])
                    ans1=input('Wants to edit(y/n)? ')
                    if ans1 in 'yY':
                            stu["Name"] = input("Enter the name :")
                            break
                    elif ans1 in 'nN':
                            break
                    else:
                            print("Press yY for YES or nN for NO.")     
                #CLASS        
                while True:
                    print('Class:',stu["Class"])
                    ans2=input('Wants to edit(y/n)? ')
                    if ans2 in 'yY':
                        stu["Class"] = input("Enter the Class :")
                        break
                    elif ans2 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                #SECTION
                while True:
                    print('Section:',stu["Section"])
                    ans3=input('Wants to edit(y/n)? ')
                    if ans3 in 'yY':
                        stu["Section"] = input("Enter the Section :")
                        break
                    elif ans3 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                #MARKS
                while True:
                    print('Marks Obtained:',stu["Total Marks"])
                    ans4=input('Wants to edit(y/n)? ')
                    if ans4 in 'yY':
                        stu["Total Marks"] = input("Enter Marks Obtained :")
                        break
                    elif ans4 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                #PERCENTAGE
                while True:
                    print('Percentage:',stu["Percentage"])
                    ans5=input('Wants to edit(y/n)? ')
                    if ans5 in 'yY':
                        stu["Percentage"] = input("Enter the Percentage :")
                        break
                    elif ans5 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                #RESULT
                while True:
                    print('Result:',stu["Result"])
                    ans6=input('Wants to edit(y/n)? ')
                    if ans6 in 'yY':
                        stu["Result"] = input("Enter new Result :")
                        break
                    elif ans6 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                #ATTENDANCE
                while True:
                    print('Attendance:',stu["Attendance"])
                    ans7=input('Wants to edit(y/n)? ')
                    if ans7 in 'yY':
                         stu["Attendance"] = input("Enter Attendance :")
                         break
                    elif ans7 in 'nN':
                        break
                    else:
                        print("Press yY for YES or nN for NO.")

                pickle.dump(stu,f2)
                found=1
                break
            
            else:
                pickle.dump(stu,f2)
        except EOFError:
            break
    if found == 0:
        print("Record not found.")
    else:
        print("Record Updated.")
    f1.close()
    f2.close()
    os.remove("StudentData.dat")
    os.rename("temp.dat","StudentData.dat")

#DELETE STUDENT
def delete_stu(r_delete):
    f=open("StudentData.dat","rb")
    f1=open("Temp.dat","wb")
    found=0
    try:
        while True:
            stu = pickle.load(f)
            if stu["RollNo"] == r_delete:
                found=1
                break
            else:
                pickle.dump(stu,f1)
                
    except EOFError:
            print("")
            
    if found == 0:
        print("No Record Found with roll number:",r_delete)
    else:
        print("Record Found and deleted.")
    f.close()
    f1.close()
    os.remove("StudentData.dat")
    os.rename("Temp.dat","StudentData.dat")

#################################################################################################################################################
#################################################################################################################################################

# ADD TEACHER
def add_teacher():
    ans = "Yy"
    while ans in 'Yy':
        t_id = int(input("Enter Teacher ID: "))
        t_name = input("Enter Teacher Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        subject = input("Enter Subject: ")
        salary = float(input("Enter Salary: "))

        # Creating Dictionary
        teacher = {"TeacherID": t_id, "Name": t_name, "Age": age, "Gender": gender,
                   "Subject": subject, "Salary": salary}

        # Writing Dictionary to file
        f = open("TeacherData.dat", "ab")
        pickle.dump(teacher, f)
        f.close()

        print("Record Added Successfully.")
        ans = input('Want to enter more records. If YES then Y/y: ')

# READ TEACHER RECORD
def read_teacher():
    f = open("TeacherData.dat", "rb")
    try:
        while True:
            teacher = pickle.load(f)
            print("\n")
            print("TeacherID:", teacher["TeacherID"])
            print("Name:", teacher["Name"])
            print("Age:", teacher["Age"])
            print("Gender:", teacher["Gender"])
            print("Subject:", teacher["Subject"])
            print("Salary:", teacher["Salary"])
            print("\n")
    except EOFError:
            print("")
           
    f.close()

# SEARCH TEACHER
def search_teacher(t_search):
    f = open("TeacherData.dat", "rb")
    found = False
    try:
        while True:
            teacher = pickle.load(f)
            if teacher["TeacherID"] == t_search:
                print("TeacherID:", teacher["TeacherID"])
                print("Name:", teacher["Name"])
                print("Age:", teacher["Age"])
                print("Gender:", teacher["Gender"])
                print("Subject:", teacher["Subject"])
                print("Salary:", teacher["Salary"])
                found = True
    except EOFError:
        print("")
    if found==False:
            print("No Teacher Data Found with ID:", t_search)
    f.close()

# UPDATE TEACHER DETAILS
def update_teacher():
    f1 = open("TeacherData.dat", "rb")
    f2 = open("temp_teacher.dat", "wb")
    t_id = int(input("Enter Teacher ID to update: "))
    found = 0
    while True:
        try:
            teacher = pickle.load(f1)
            if teacher["TeacherID"] == t_id:
                print('Name:', teacher["Name"])
                ans1 = input('Wants to edit (y/n)? ')
                if ans1 in 'yy':
                    teacher["Name"] = input("Enter the name: ")

                print('Age:', teacher["Age"])
                ans2 = input('Wants to edit (y/n)? ')
                if ans2 in 'yy':
                    teacher["Age"] = int(input("Enter the age: "))

                print('Gender:', teacher["Gender"])
                ans3 = input('Wants to edit (y/n)? ')
                if ans3 in 'yy':
                    teacher["Gender"] = input("Enter the gender: ")

                print('Subject:', teacher["Subject"])
                ans4 = input('Wants to edit (y/n)? ')
                if ans4 in 'yy':
                    teacher["Subject"] = input("Enter the subject: ")

                print('Salary:', teacher["Salary"])
                ans6 = input('Wants to edit (y/n)? ')
                if ans6 in 'yy':
                    teacher["Salary"] = float(input("Enter the salary: "))

                pickle.dump(teacher, f2)
                found = 1
                break
            else:
                pickle.dump(teacher, f2)
        except EOFError:
            break

    if found == 0:
        print("Record not found.")
    else:
        print("Record Updated.")

    f1.close()
    f2.close()
    os.remove("TeacherData.dat")
    os.rename("temp_teacher.dat", "TeacherData.dat")

# DELETE TEACHER
def delete_teacher(t_delete):
    f = open("TeacherData.dat", "rb")
    f1 = open("Temp_teacher.dat", "wb")
    found = 0
    try:
        while True:
            teacher = pickle.load(f)
            if teacher["TeacherID"] == t_delete:
                found = 1
                break
            else:
                pickle.dump(teacher, f1)
    except EOFError:
        print("")
    if found == 0:
        print("No Record Found with Teacher ID:", t_delete)
    else:
        print("Record Found and deleted.")
    f.close()
    f1.close()
    os.remove("TeacherData.dat")
    os.rename("Temp_teacher.dat", "TeacherData.dat")


##################################################################################################################################################

# ADD FEE DETAILS
def add_fee():
    ans = "Yy"
    while ans in 'Yy':
        student_id = int(input("Enter Student ID: "))
        monthly_fee = float(input("Enter Monthly Fee: "))
        bus_fee = float(input("Enter Bus Fee: "))
        lab_fee = float(input("Enter Lab Fee: "))
        main_fee = float(input("Enter Maintenance Fee: "))

        total_fee = monthly_fee + bus_fee + lab_fee +  main_fee 

        # Creating Dictionary
        fee_data = {
            "StudentID": student_id,
            "MonthlyFee": monthly_fee,
            "BusFee": bus_fee,
            "LabFee": lab_fee,
            "MainFee": main_fee,
            "TotalFee": total_fee
        }

        # Writing Dictionary to file
        f = open("FeeData.dat", "ab")
        pickle.dump(fee_data, f)
        f.close()

        print("Fee Record Added Successfully.")
        ans = input('Want to enter more fee records. If YES then Y/y: ')

# UPDATE FEE DETAILS
def update_fee():
    f1 = open("FeeData.dat", "rb")
    f2 = open("temp_fee.dat", "wb")
    s_id = int(input("Enter Student ID to update fee: "))
    found = 0
    while True:
        try:
            fee_data = pickle.load(f1)
            if fee_data["StudentID"] == s_id:
                
                print('Monthly Fee:', fee_data["MonthlyFee"])
                ans2 = input('Wants to edit (y/n)? ')
                if ans2 in 'Yy':
                    fee_data["MonthlyFee"] = float(input("Enter new Monthly Fee: "))

                print('Bus Fee:', fee_data["BusFee"])
                ans3 = input('Wants to edit (y/n)? ')
                if ans3 in 'Yy':
                    fee_data["BusFee"] = float(input("Enter new Bus Fee: "))

                print('Lab Fee:', fee_data["LabFee"])
                ans4 = input('Wants to edit (y/n)? ')
                if ans4 in 'Yy':
                    fee_data["LabFee"] = float(input("Enter new Lab Fee: "))

                print('Maintenance Fee:', fee_data["MainFee"])
                ans1 = input('Wants to edit (y/n)? ')
                if ans1 in 'Yy':
                    fee_data["MainFee"] = float(input("Enter new Maintenance Fee: "))



                fee_data["TotalFee"] = (fee_data["MonthlyFee"] + fee_data["BusFee"] + fee_data["LabFee"] + fee_data["MainFee"])

                pickle.dump(fee_data, f2)
                found = 1
                break
            else:
                pickle.dump(fee_data, f2)
        except EOFError:
            break

    if found == 0:
        print("Record not found with student ID:",s_id)
    else:
        print("Fee Record Updated.")

    f1.close()
    f2.close()
    os.remove("FeeData.dat")
    os.rename("temp_fee.dat", "FeeData.dat")

# DISPLAY ALL FEE DATA
def display_fee():
    f = open("FeeData.dat", "rb")
    try:
        while True:
            fee_data = pickle.load(f)
            print("\n")
            print("StudentID:", fee_data["StudentID"])
            print("Monthly Fee:", fee_data["MonthlyFee"])
            print("Bus Fee:", fee_data["BusFee"])
            print("Lab Fee:", fee_data["LabFee"])
            print("Maintenance Fee:", fee_data["MainFee"])
            print("Total Fee:", fee_data["TotalFee"])
            print("\n")
    except EOFError:
            print("")


# ADD BOOK
def add_book():
    ans = "Yy"
    while ans in 'Yy':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
    
        # Creating Dictionary
        book = {"BookID": book_id,"Title": title}

        # Writing Dictionary to file
        f = open("LibraryData.dat", "ab")
        pickle.dump(book, f)
        f.close()

        print("Book Added Successfully.")
        ans = input('Want to add more books. If YES then Y/y: ')

# REMOVE BOOK
def remove_book():
    book_id = int(input("Enter Book ID to remove: "))
    f1 = open("LibraryData.dat", "rb")
    f2 = open("temp_library.dat", "wb")
    found = 0
    while True:
        try:
            book = pickle.load(f1)
            if book["BookID"] == book_id:
                found = 1
            else:
                pickle.dump(book, f2)
        except EOFError:
            break

    f1.close()
    f2.close()

    if found == 1:
        os.remove("LibraryData.dat")
        os.rename("temp_library.dat", "LibraryData.dat")
        print("Book Removed Successfully.")
    else:
        print("No Book Found with Book ID:", book_id)

# DISPLAY ALL BOOKS
def display_books():
    f = open("LibraryData.dat", "rb")
    try:
        while True:
            book = pickle.load(f)
            print("Available Books in the Library are: \n")
            print("BookID:", book["BookID"])
            print("Title:", book["Title"])
            print("\n")
    except EOFError:
            print("")
            
    f.close()


heading()
main_menu()
while True:
    menu_choice=int(input("Enter Choice:"))
    if menu_choice == 1:
        while True:
            student()
            choice_stu=int(input("Enter Your Choice:"))
            if choice_stu==1:
                add_stu()
            elif choice_stu==2:
                r_search=int(input("Enter roll no to search:"))
                search_stu(r_search)
            elif choice_stu==3:
                r_delete=int(input("Enter roll no to delete:"))
                delete_stu(r_delete)
            elif choice_stu==4:
                update_stu()
            elif choice_stu==5:
                read_stu()
            elif choice_stu==6:
                main_menu()
                break
            else:
                print("Enter Correct Choice.")
    elif menu_choice == 2:
        while True:
            teacher()
            choice_tea=int(input("Enter Your Choice:"))
            if choice_tea == 1:
                add_teacher()
            elif choice_tea == 2:
                t_search=int(input("Enter teacher's ID to search:"))
                search_teacher(t_search)
            elif choice_tea == 3:
                t_delete=int(input("Enter teacher's ID to delete:"))
                delete_teacher(t_delete)
            elif choice_tea == 4:
                update_teacher()
            elif choice_tea == 5:
                read_teacher()
            elif choice_tea == 6:
                main_menu()
                break
            else:
                print("Enter Correct Choice.")
    elif menu_choice == 3:
        while True:
            print("\n")
            print("1. FEES MANAGEMENT")
            print("2. LIBRARY MANAGEMENT")
            print("3. BACK TO PREVIOUS SLIDE")
            print("\n")
            
            choice_others=int(input("Enter Your Choice:"))
            if choice_others == 1:
                while True:
                    fee_structure()
                    choice_fee=int(input("Enter Your Choice:"))
                    if choice_fee == 1:
                        add_fee()
                    elif choice_fee == 2:
                        update_fee()
                    elif choice_fee == 3:
                        display_fee()
                    elif choice_fee == 4:
                        break
                    else:
                        print("Enter Correct Choice.")

                    
            elif choice_others == 2:
                while True:
                    library_management()
                    choice_lib=int(input("Enter Your Choice:"))
                    if choice_lib == 1:
                        add_book()
                    elif choice_lib == 2:
                        remove_book()
                    elif choice_lib == 3:
                        display_books()
                    elif choice_lib == 4:
                        break 
                    else:
                        print("Enter Correct Choice.")
                

            elif choice_others == 3:
                main_menu()
                break
            
            else:
                print("Enter Correct Choice.")
                    
                    
    elif menu_choice == 4:
        print("THANKS FOR USING OUR PROGRAM")
        break
    else:
        print("Enter Correct Choice.")     
