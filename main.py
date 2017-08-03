#Seong Ma


import re, os, send2trash
import input_functions

'''
This program will ask the user to enter the name of a valid directory
and then ask for the user to input_functions a string, all files with a filename 
that contains the string will be sent to the recycle bin
'''

if __name__ == '__main__':
    while True:
        directory = input_functions.get_directory()
        if directory.lower() == 'q':
            break
        
        delete_key = input_functions.get_delete_key()
        
        delete_re = re.compile(r"""^(.*?)""" + delete_key + r"""(.*?)""", re.VERBOSE)
        
        print("DELETING: ")
        
        for filename in os.listdir(directory):
            delete_match = delete_re.search(filename)
            if delete_match != None:
                absolute_file_directory = os.path.abspath(directory)
                filename = os.path.join(absolute_file_directory, filename)
                print(filename)
                send2trash.send2trash(filename)
        print('\n')
                