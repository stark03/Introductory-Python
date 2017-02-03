import os
import string
def rename_files():
    list_of_file = os.listdir(r"C:\Users\Tushar Murarka\Desktop\Python\prank")
    savedpath = os.getcwd()
    os.chdir(r"C:\Users\Tushar Murarka\Desktop\Python\prank")
  
    for file in list_of_file:
        trans = file.maketrans("" , "" , string.digits)
        os.rename(file , file.translate(trans))
        print(file)
        print("\n")
    os.chdir(savedpath)

rename_files()
