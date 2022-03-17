import pathlib
from sys import *
import os

########################################################################################################################
## Function name :  DirectoryWatcher   
## Input :          path
## Output :         Rename files with specific extension
## Description :    This Script is used to traverse specific directory and to rename files with specific extension
## Author :         Girish Pradeep Patil
## Date :           07/02/2022
########################################################################################################################

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)           

            for filen in filname:
                #print(filen)
                p=pathlib.Path('%s'% filen)
                print(pathlib.Path(str(p).removesuffix(''.join(p.suffixes))).with_suffix('%s'%argv[2]))
                
                
            print('')

    else:
        print("Invalid Path")


########################################################
## Starter function for DirectoryWatcher function
######################################################## 
def main():
    print("---- Girish Patil : Automation Script-----")

    print("Application name : " +argv[0])

    if (len(argv) !=3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and to rename files with specific extension")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name AbsolutePath_of_Directory Rename_File_With_Specific_Extension")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype input")

    except Exception:
        print("Error : Invalid Input")

if __name__ == "__main__":
    main()
