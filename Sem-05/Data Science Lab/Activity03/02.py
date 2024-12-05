def count_file_content(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the file name to count content: ")
    count_file_content(filename)
