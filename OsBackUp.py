# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:40:48 2020

@author: jacks
"""

# Python program to explain shutil.copytree() method  
       
# importing os module  
import os  
   
# importing shutil module  
import shutil  
   
"""# path  
path = 'C:/Users/jacks/Downloads'
   
# List files and directories  
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'  
print("Before copying file:")  
print(os.listdir(path))  
   """
   
# Source path  
print("Enter the directory you want to back up, Ex: C:/Users/jacks : ")
src = input()
   
# Destination path  
print(os.listdir("D:/"))
print("Specify where you want the backup: (FOLDER HAS TO BE UNIQUE, BECAUSE IT WILL BE CREATED DURING SORTING, NO DUPES EX: D:/BackUpFolder")
dest = input()
   
# Copy the content of  
# source to destination  
destination = shutil.copytree(src, dest)  
   
# List files and directories  
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"  
'''print("After copying file:")  
print(os.listdir(path)) ''' 
   
# Print path of newly  
# created file  
print("Destination path:", destination) 