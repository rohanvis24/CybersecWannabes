import tkinter as tk
import os
#import matplotlib as mp
#import matplotlib.pyplot as plot

# User password
userPassword = ""

# Cross-function boolean trackers
isWrong = False
isRight = False
endProgram = False

# Attempt counter
attemptCtr = 0

# Becomes true if the user inputs the correct password
isCorrect = False

# Establishing a few global variables to use as the information passes between functions
tempVar1 = ""
tempvar2 = ""
tempVar3 = ""

def submitNewUserPassword():
        global userPassword
        
        newPass = newUserEntry.get()
        passFile.write(newPass + "\n")
        userPassword = newPass
        newUserWindow.destroy()
        introFunction()
        
def introFunction():
        # Declaration that we're using global variables
        global userPassword
        #global tempVar1
        #global tempVar2
        
        # Starts the intro screen asking the user for the password
        introWindow = tk.Tk()
        introWindow.geometry("1280x840")
        introLabel = tk.Label(text="Enter your password: ")
        introEntry = tk.Entry(width=50)
        introButton = tk.Button(text="Submit", width=25, height=5, bg="green", fg="orange", command=lambda:introOnClick(introEntry.get(), introWindow, introLabel, introEntry, introButton))
        
        introLabel.pack()
        introEntry.pack()
        introButton.pack()
        
        introWindow.mainloop()
        
        #while True: #constant loop checking for variable updates
         #   if endProgram: # runs if the user ran out of attempts
          #          print("endProgram updated") #debug statement
            #        print("Program terminated")
             #       introWindow.destroy()
            #if isWrong: # runs if the password entered is wrong
             #       print("isWrong update") #debug statement
              #      isWrong = False
               #     introEntry.delete(0, tk.END)
            #if isRight: # runs if the password entered is right
             #       print("isRight update") #debug statement
              #      introWindow.destroy()
               #     passwordManagerViewer()
        
def introOnClick(userEnteredPassword, inputWindow, inputLabel, inputEntry, inputButton):
        global attemptCtr
        
        if userEnteredPassword == userPassword:
            print("Access granted")
            inputWindow.destroy()
            passwordManagerViewer()
            
        else: # Wrong password
            attemptCtr += 1
            print("Incorrect! You have " + str(10-attemptCtr) + " attempts left :/")
            if attemptCtr == 10:
                print("Omae wa mou, shindeiru")
                inputWindow.destroy()
            else:
                inputEntry.delete(0, tk.END)
            
       #introEntry.delete(0, tk.END)
    
def passwordManagerViewer():
    passManWindow = tk.Tk()
    passManWindow.geometry("1280x840")
    
    passManWindow.mainloop()


# Main function
with open("passwordList.txt", "r+") as passFile:
    passFileDump = passFile.readlines()
    for i in range(len(passFileDump)):
        passFileDump[i] = passFileDump[i].strip("\n")
    
    # Lets the new user set their password
    if passFileDump[0].strip("\n") == '': # The password file is completely empty
        
        # Pop up a window prompting the user to input their new password
        # Possible double check on password (for correct syntax)
        newUserWindow = tk.Tk()
        newUserWindow.geometry("1280x840")
        newUserLabel = tk.Label(text="Enter a new password: ")
        newUserEntry = tk.Entry(width=50)
        newUserButton = tk.Button(text="Submit", width=25, height=5, command = submitNewUserPassword)
        
        # Pack up all of the compnents of the window and show it
        newUserLabel.pack()
        newUserEntry.pack()
        newUserButton.pack()
        
        newUserWindow.mainloop()
    
    # Returning user
    else: # There is an existing password
        # Gets the line with the password
        print(passFileDump)
        userPassword = passFileDump[0]
        
        introFunction()
        
'''
        while True:
                if isCorrect:
                    # This should grant the user access to all of the passwords stored
                    print("lol")
                    break
'''
    
