def read_and_display_file(filename):
    """Reads the content of a file and displays it on the screen."""
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            print("File Content:")
            print(content)  # Display the content on the screen
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the file name to read: ")
    read_and_display_file(filename)
