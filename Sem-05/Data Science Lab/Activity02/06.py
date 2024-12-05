# main.py

import file_operations  # Import the file_operations module

def test_file_operations():
    filename = 'sample.txt'
    
    if not file_operations.file_exists(filename):
        print(f"The file {filename} does not exist.\n")
    
    content_to_write = "This is a sample file.\nIt contains some text data."
    file_operations.write_to_file(filename, content_to_write)
    
    print("\nReading content from the file:")
    content = file_operations.read_from_file(filename)
    if content:
        print(content)
    
    content_to_append = "\nThis is additional content appended to the file."
    file_operations.append_to_file(filename, content_to_append)
    
    print("\nReading the file line by line:")
    lines = file_operations.read_lines_from_file(filename)
    if lines:
        for line in lines:
            print(line.strip())  # Print each line after stripping trailing whitespace

if __name__ == "__main__":
    test_file_operations()
