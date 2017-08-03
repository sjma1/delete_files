import os

def valid_directory(path: str):
    return os.path.exists(path) and os.path.isdir(path)
    
def get_directory():
    while True:
        temp = input("Enter a valid directory (Q to quit): ")
        if valid_directory(temp) or temp.lower() == 'q':
            return temp
        print("INVALID DIRECTORY!\n")
        
def get_delete_key():
    while True:
        delete_key = input("Enter the string to use for file deletion: ")
        
        confirm = input("All files containing the string \'" + delete_key + "\' will be deleted(y/n)")
        if confirm.lower() == 'y':
            return delete_key
        print('\n')