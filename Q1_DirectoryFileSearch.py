from sys import *
import os
#import pathlib
#import glob

########################################################################################################################
## Function name :  DirectoryWatcher   
## Input :          path
## Output :         Files with specific extension
## Description :    This Script is used to traverse specific directory and to display files with specific extension
## Author :         Girish Pradeep Patil
## Date :           07/02/2022
########################################################################################################################

def DirectoryWatcher(path):


    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):        # Travel directory
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)           

            for filen in filname:
                splitting=filen.split('.')

                if splitting[1]==argv[2][1:]:
                    print("Files with extension",argv[2],"in",foldername,"are",filen)     
                
            print('')

    else:
        print("Invalid Path")

    #fileExt=".%s"                                          optional case
    
    #specific=list(pathlib.Path(path).glob(fileExt))
    #print("Files with specific extension are: ",specific)



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
        print("This Script is used to traverse specific directory and to display files with specific extension")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name AbsolutePath_of_Directory Specific_Extension_File_Display")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype input")

    except Exception:
        print("Error : Invalid Input")

if __name__ == "__main__":
    main()
