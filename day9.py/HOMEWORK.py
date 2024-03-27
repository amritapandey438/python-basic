import os

def create_file(filename):
    with open(filename, 'w') as file:
        print("File created successfully.")

def write_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print("Content written to file successfully.")

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

def append_to_file(filename, additional_content):
    with open(filename, 'a') as file:
        file.write("\n" + additional_content)
    print("Additional content appended to file successfully.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")

def main():
    filename = input("Enter the name of the file: ")

    # Create file
    create_file(filename)

    # Write content to file
    content = input("Enter the content you want to write to the file: ")
    write_to_file(filename, content)

    # Read file
    read_file(filename)

    # Append additional content to file
    additional_content = input("Enter additional content to append to the file: ")
    append_to_file(filename, additional_content)

    # Read file again after appending
    read_file(filename)

    # Delete file
    delete_option = input("Do you want to delete the file? (yes/no): ")
    if delete_option.lower() == "yes":
        delete_file(filename)
    else:
        print("File not deleted.")

if __name__ == "__main__":
    main()