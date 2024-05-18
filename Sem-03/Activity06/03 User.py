import hashlib

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_login(self, username, password):
        if username == self.__username and self.__hash_password(password) == self.__password:
            return True
        else:
            return False

user = User("example_user", "password123")

print(user.validate_login("example_user", "password123"))  # Output: True
print(user.validate_login("example_user", "wrong_password"))  # Output: False
