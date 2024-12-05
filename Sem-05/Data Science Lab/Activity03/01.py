def append_text_to_file(filename, text_to_append):
    """Appends text to an existing file."""
    try:
        with open(filename, 'a') as file:
            file.write(text_to_append + '\n')  # Append the text with a newline at the end
            print(f"Text successfully appended to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the file name to append text to: ")
    text_to_append = input("Enter the text you want to append: ")
    append_text_to_file(filename, text_to_append)
