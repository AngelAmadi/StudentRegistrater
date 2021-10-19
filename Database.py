import pickle # pickle is a storing agent storing agent
from tkinter import *
# for my graphical user interface
# gui create a GUI window

receptionist= [
"Remi Floyd",
"Corrina Carroll",
"Franco Gillespie",
"Finbar Campos",
"Nadia Oconnell",
"Theia Mcbride",
"Anastazja Copeland",
"Nadia Oconnell",
"Orla Mcdougall",
"Shanay Walls"]

window = Tk()
window.title("Receptionist names")  
window.geometry("360x150") #width, height
window.configure(bg='#ffdab9')

text = Label(window, text="Pick your name from the below names:\nAfter picking click button", bg='#ffdab9')
text.place(x=40,y=10) #left+right,up and down the axis

drop_down = StringVar(window) # a class that provides helper functions to access the menu
drop_down.set(receptionist[0]) # default value drop_down

menu = OptionMenu(window, drop_down, *receptionist)
menu.place(x=100,y=60) 

def end (): 
    window.destroy() # when the command end is called upon it will end gui 

button = Button(window, text="Click to progress into program to access student details", command=end)
button.place(x=4,y=80)

mainloop()

#Set a password for the school only login in
def begin():
    count=0
    while count <3:
 #limiting log in to 3 attempts  
        userName = input ("Enter Username: ")
        passWord = input ("Enter Password: ")
        if userName == 'NTU_School' and passWord == 'comp2ii':
            print ("YOU MUST SAVE ALL DOCUMENTS WHEN ANY ACTIVITY IS CARRIED OUT!")
            login() #break into code 

        else:
            print ("Invalid login details!")
            count = count +1
    print ("Access declined, try again later.")

def login():
    option = None # no situation which there wont be  
    student =  {"Aliya Corrigan":"SC12", 
            "Kavan Serrano":"SC13", 
             "Vanessa Gray" :"SC14", 
             "Shona Duffy" :"SC15", 
            "Izabella Wong" :"SC16",
            "Chris Monaghan" :"SC17", 
            "Jose Torres" :"SC18", 
            "Jordana Snyder":"SC19",
           "Humza Mohammed" :"SC20"}
    

    while option != "0":
            print("""
                    The school online file registery 
                   --------------------------------------------------------
                    PICK AN OPTION BELOW TO BROWSE THE SYSTEM
                    1 . Find out the registeration details if registered
                    2 . Register a new student by their details 
                    3 . save any any done in database 
                    4 . load all students and details in the school system
                    5 . replace/update any student's ID
                    6 . delete student
                    0 . log out of system 
                    --------------------------------------------------------
            """)
            
            option = input("Pick from option 1-0: ")
           
            # Find out the registeration
            if option == "1":
                    print("Here are all of your students who have registered: ")
                    for name in student:
                            print(name)
                    identity = input("Name of student you want their details? ")
                    details = identity.title()
                    if details in student:
                            print(details,"'s student number is ",student[details])
                    else:
                            print("Student not registered,type 2 from the main option to register a student by allocating a student number")

            # Register a student by adding details
            elif option == "2":
                    newStudent = input("What is the name of the students ?")
                    new_s_C= newStudent.title() # caps on first letter
                    print("What is ", new_s_C, "'s student ID? ")
                    newID = input("Put number here correctly: ")
                    if len(newID) == 4: 
                        newIDS = newID.upper()
    
                    else:
                        newID = input("Enter a valid Student ID consisting of 4 letters/numbers: ")
                        
                    
                    newIDS = newID.upper()
                    student.update({new_s_C :newIDS })
                    print("\nYou assigned ", new_s_C , " to this ID number ",newIDS)
                    print ("You MUST press 3 now to save in the database!!")
            
            # save 
            elif option == "3":
                    pickle.dump(student, open("student.pkl", "wb")) 
                    # wb means write the file in binary , student.pkl is my file 
                    print("All the students are saved, check option 4 from the main menu for updated list")

           # load 
            elif option == "4":
                    student = pickle.load(open("student.pkl", "rb")) # rb means read the file in binary  
                    if student:
                            for item, value in student.items(): # calls on dict pairs and print them
                                    print(item,": ", value)
                    else:
                            print(" ")

            #updated/replace ID
            elif option == "5":
                    print("All the students the school has on the system include: ")
                    if student:
                            for item in student:
                                    print(item)
                            studentRplc = input("Which student would you like to update their student ID? ")
                            studentRplc_C = studentRplc.title()
                            if studentRplc_C in student:
                                    print(studentRplc_C, " is registered with ", student[studentRplc_C], " at the moment ")
                                    repID = input("What is the new student ID for the name you chose? ")

                                    
                                    if len(repID) == 4: 
                                        repID_C = repID.upper()
    
                                    else:
                                        repID = input("Enter a valid Student ID consisting of 4 letters/numbers: ")
                        
                    
                                    repID_C = repID.upper()
                                    student[studentRplc_C] = repID_C
                                    print( studentRplc_C, "'s new student ID is now ", repID_C)
                                    print ("You MUST press 3 now to save in the database!!")
                                    
                            else:
                                    print("Student not found in the school system, you can add a new student by press number 2 from the main menu")
                    else:
                            print(" ")

            # delete 
            elif option == "6":
                    print("Want to delete a student from the system ?")
                    del_stu = input("Enter student's name : ")
                    del_stuC= del_stu.title()
                    if del_stuC in student:
                            lastChance = input("\nAre you sure you want to delete this student ? Yes or No : ")
                            lastChanceCaps = lastChance.upper()
                            if lastChanceCaps == "YES":
                                    del student[del_stuC]
                                    print("Student has been deleted!")
                                    print ("You MUST press 3 now to save in the database!!")
                            else:
                                    print("Student was not deleted!")
                    else:
                            print("That student does not exist.")
                            
            # log out
            elif option == "0":
                    print("BYE-BYE..")
                    quit()
            # invalid option
            else:
                    print("\nSorry", option ,"isn't a valid option.")
                  
begin()

