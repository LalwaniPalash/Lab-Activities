def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def to_upper_case(s):
    """Converts all characters in the string to uppercase."""
    return s.upper()

def to_lower_case(s):
    """Converts all characters in the string to lowercase."""
    return s.lower()

def remove_whitespace(s):
    """Removes leading and trailing whitespace from the string."""
    return s.strip()

def replace_spaces_with_underscore(s):
    """Replaces all spaces in the string with underscores."""
    return s.replace(" ", "_")

def count_vowels(s):
    """Counts the number of vowels (a, e, i, o, u) in the string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Checks if the given string is a palindrome."""
    return s == reverse_string(s)
