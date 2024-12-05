from google.colab import drive

drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/sample.txt'

with open(file_path, 'w') as file:
    file.write("Hello, Google Drive!\nThis is a sample file created and written from Google Colab.")

print(f"File successfully written to {file_path}")
