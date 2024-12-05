def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    input_string = "hello"
    result = reverse_string(input_string)
    print(f"The reversed string of '{input_string}' is: '{result}'")
