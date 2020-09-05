import tkinter as tk
import os
import matplotlib as mp
import matplotlib.pyplot as plot

def introOnClick():
        global attemptCtr
        userText = entry.get()
        if userText == userPassword:
            print("Access granted")
            attemptCtr = 0
        else:
            attemptCtr += 1
            print("Incorrect! You have " + str(10-attemptCtr) + " attempts left :/")
        
        entry.delete(0, tk.END)
        if attemptCtr == 10:
            print("Omae wa mou, shindeiru")
            introWindow.destroy()



with open("password.txt", "rwa") as passFile:
    
    # Password to access the database
    userPassword = "password"
    
    # Attempt counter
    attemptCtr = 0
    
    # Becomes true if the user inputs the correct password
    isCorrect = False
    
    # Starts the intro screen asking the user for the password
    introWindow = tk.Tk()
    #greeting = tk.Label(text="heck", bg="#500000")
    entry = tk.Entry(width=50)
    button = tk.Button(text="Submit", width=25, height=5, bg="green", fg="orange", command = introOnClick)
    
    #greeting.pack()
    button.pack()
    entry.pack()
    
    window.mainloop()
    
    while True:
            if isCorrect:
                # This should grant the user access to all of the passwords stored
            
            
