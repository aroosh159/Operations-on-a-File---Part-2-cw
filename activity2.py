file = open('New_file.txt','x')
file.close()

import os 
if os.path.exists("My_file.txt"):
    print("file exists")
else:
    print("The file doesnot exists")
file = open('My_file.txt','w')
os.remove('codingaltext.txt')
