import time
import mysql.connector
from sys import argv as line

username = input("Database Username: ")
password = input("Database Password: ")

db = mysql.connector.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="medicaldb"
    )
db_cursor = db.cursor()
    
def pat_error():
    print("-----ERROR-----")

def success():
    print("======Success======")

# Var
usr_id = ""
auth = False
user_auth = True
edit_loop = True

def add_pat():
    print("=====================")
    add_pat_firstname = input("New Patient's First Name: ")
    add_pat_lastname = input("New Patient's Last Name: ")
    add_pat_sex = input("New Patient's Sex M/F: ")
    add_pat_h = input("New Patient's Height(xxx.xx): ")
    add_pat_w = input("New Patient's Weight(xxx.xx): ")
    add_pat_result = input("New Patient's Result(positive/negative/empty): ")
    pat_add_sql = ("INSERT INTO patient (FirstName, LastName, Sex, Height, Weight, Result) VALUES (%s, %s, %s, %s, %s, %s)")
    pat_add_val = (add_pat_firstname, add_pat_lastname, add_pat_sex, add_pat_h, add_pat_w, add_pat_result)
    
    
    db_cursor.execute(pat_add_sql, pat_add_val)
    db.commit()

            
def search_pat():
    print("=====================")
    lookup_name = input("Search Patient's ID: ")
    pat_lookup = "SELECT * FROM patient WHERE ID="+lookup_name
    
    db_cursor.execute(pat_lookup)
    for x in db_cursor:
        ID, FirstName, LastName, Sex, Height, Weight, Result = x
        print("Patient's ID: ", ID,"\nPatient's First Name: ", FirstName,"\nPatient's Last Name: ", LastName,"\nPatient's Sex: ", Sex,"\nPatient's Height: ", Height,"\nPatient's Weight: ", Weight,"\nPatient's COVID Result: ", Result)
                
                       
def edit_pat():
    print("=====================")
    lookup_name = input("Search Patient's ID: ")
    pat_lookup = "SELECT * FROM patient WHERE ID="+lookup_name
    
    db_cursor.execute(pat_lookup)
    for x in db_cursor:
        ID, FirstName, LastName, Sex, Height, Weight, Result = x
        print("=====================")
        print("Patient's ID: ", ID,"\nPatient's First Name: ", FirstName,"\nPatient's Last Name: ", LastName,"\nPatient's Sex: ", Sex,"\nPatient's Height: ", Height,"\nPatient's Weight: ", Weight,"\nPatient's COVID Result: ", Result)
    edit_loop = True
    while edit_loop:
        print("1: First Name \n2: Last Name \n3: Sex \n4: Height \n5: Weight \n6: COVID Result \nAny Key to Exit")
        edit_select = input("What would you like to edit: ")
        if edit_select == "1":
            FirstName = input("New First Name: ")
            update_pat = ("UPDATE patient SET FirstName = %s WHERE ID = %s")
            update_pat_var = (FirstName, lookup_name)
            print(update_pat, update_pat_var)
    
            db_cursor.execute(update_pat, update_pat_var)
            db.commit()
        elif edit_select == "2":
            LastName = input("New Last Name: ")
            update_pat = ("UPDATE patient SET LastName = %s WHERE ID = %s")
            update_pat_var = (LastName, lookup_name)
            print(update_pat, update_pat_var)
            try:
                db_cursor.execute(update_pat, update_pat_var)
                db.commit()
            except:
                pat_error()
                edit_loop = False
        
        elif edit_select == "3":
            LastName = input("Change Sex: ")
            update_pat = ("UPDATE patient SET Sex = %s WHERE ID = %s")
            update_pat_var = (Sex, lookup_name)
            print(update_pat, update_pat_var)
            try:
                db_cursor.execute(update_pat, update_pat_var)
                db.commit()
            except:
                pat_error()
                edit_loop = False
        elif edit_select == "4":            
            LastName = input("Change Height: ")
            update_pat = ("UPDATE patient SET Height = %s WHERE ID = %s")
            update_pat_var = (Height, lookup_name)
            print(update_pat, update_pat_var)
            try:
                db_cursor.execute(update_pat, update_pat_var)
                db.commit()
            except:
                pat_error()
                edit_loop = False
        elif edit_select == "5":
            LastName = input("Change Weight: ")
            update_pat = ("UPDATE patient SET Weight = %s WHERE ID = %s")
            update_pat_var = (Weight, lookup_name)
            print(update_pat, update_pat_var)
            try:
                db_cursor.execute(update_pat, update_pat_var)
                db.commit()
            except:
                pat_error()
                edit_loop = False
        elif edit_select == "6":
            LastName = input("Update COVID Result: ")
            update_pat = ("UPDATE patient SET Result = %s WHERE ID = %s")
            update_pat_var = (Result, lookup_name)
            print(update_pat, update_pat_var)
            try:
                db_cursor.execute(update_pat, update_pat_var)
                db.commit()
            except:
                pat_error()
                edit_loop = False
        else:
            edit_loop = False

   

# Welcome Message
print("Welcome to the Medical Database")
auth = True
time.sleep(.2)

# Main Menu Loop
while auth:
    
    # Menu Selector
    print("=====================")
    print("1: Add New Resultn\n2: Search the Database\n3: Edit Patient\n4: Exit Program")
    print("=====================")
    action = input("What do you want to do? ")
    
    
    # Adding Patients
    if action == "1":
        add_pat()

    # Searching for Patients
    elif action == "2":
        search_pat()
              
    # Edit Patient
    elif action == "3":
        edit_pat()
 
     # Exit Program
    elif action == "4":
        print("Thank you! Come again soon,",username)
        print("=====================")
        auth = False


    # Error Code
    elif action != (1,2,3,4):
        print("Error: Option Not Found")