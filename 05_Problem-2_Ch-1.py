# Here is a Python program that uses the os module to print the contents of a directory:
import os

def list_directory_contents(directory_path):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the directory path from the user
    path = input("Enter the path of the directory you want to list: ").strip()
    list_directory_contents(path)
