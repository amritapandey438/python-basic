# Global variable to store data
data_list = []

def add_data():
    global data_list
    title = input("Enter title: ")
    description = input("Enter description: ")
    data_list.append((title, description))
    print("Data added successfully!")

def view_all_data():
    global data_list
    if data_list:
        print("All Data:")
        for idx, data in enumerate(data_list, start=1):
            print(f"{idx}. Title: {data[0]}, Description: {data[1]}")
    else:
        print("No data available.")

# Main function to interact with the user
def main():
    while True:
        print("\n1. Add Data")
        print("2. View All Data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            view_all_data()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()