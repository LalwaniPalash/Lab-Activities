class PasswordValidator:
    minimumLength = 8

    def is_valid(self, password):
        if len(password) < PasswordValidator.minimumLength:
            return False

        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)

        return has_uppercase and has_lowercase and has_digit

validator = PasswordValidator()

password1 = "Password123"
password2 = "password"    
password3 = "12345678"
password4 = "PASSWORD"
password5 = "Password"


print("Password 1 validity:", validator.is_valid(password1))
print("Password 2 validity:", validator.is_valid(password2))
print("Password 3 validity:", validator.is_valid(password3))
print("Password 4 validity:", validator.is_valid(password4))
print("Password 5 validity:", validator.is_valid(password5))
