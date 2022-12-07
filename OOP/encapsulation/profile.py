import re


class Profile:
    __PASSWORD_PATTERN = '(?=[A-Za-z0-9+)^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,}).*$'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" ' \
               f'and password: {"".join(["*" for _ in range(len(self.password))])}'

    @staticmethod
    def is_password_valid(password):
        return len(password) >= 8 \
               and re.search(Profile.__PASSWORD_PATTERN, password)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError(f"The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not self.is_password_valid(value):
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
