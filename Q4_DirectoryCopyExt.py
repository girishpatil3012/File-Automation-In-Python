from sys import *
import os
import shutil

#####################################################################################################################################
## Function name :  DirectoryWatcher   
## Input :          path
## Output :         Copy files of specific extension from one directory to another
## Description :    This Script is used to copy files of specific extension from one directory and to paste into another directory
## Author :         Girish Pradeep Patil
## Date :           07/02/2022
####################################################################################################################################

def DirectoryWatcher(path):

    flag = os.path.isabs(path)                              # Directory Travel
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        os.mkdir(argv[2])
        print("Directory %s is built at Runtime" % argv[2])

        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)           

            for filen in filname:
                splitting=filen.split('.')

                if splitting[1]==argv[3][1:]:
                    print("Files with extension",argv[3],"in",foldername,"are",filen)
                    shutil.copy2(os.path.join(path,filen),argv[2])
                
            print('')

    else:
        print("Invalid Path")


########################################################
## Starter function for DirectoryWatcher function
########################################################
def main():
    print("---- Girish Patil : Automation Script-----")

    print("Application name : " +argv[0])

    if (len(argv) !=4):
        print("Error : Invalid number of argumentss")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to copy files of specific extension from one directory and to paste into another directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Copy_Files_of_Specific_Extension_From_One_Directory_To_Another")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype input")

    except Exception:
        print("Error : Invalid Input")

if __name__ == "__main__":
    main()
