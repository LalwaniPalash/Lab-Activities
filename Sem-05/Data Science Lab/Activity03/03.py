def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Content successfully copied from {source_file} to {destination_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    copy_file_content(source_file, destination_file)
