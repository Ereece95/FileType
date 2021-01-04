# Eric Reece - 1/3/2021
# This program simply accepts a user-provided file (etc. test.java), and prints the extension.
# Very simple, just wanted to practice with the split function.
if __name__ == '__main__':
    # Obtains user file, splits at the start of the extension
    file_name = input("Enter a file name:\n")
    file_type = file_name.split('.')

    print("Your file is type: ", file_type[1])
