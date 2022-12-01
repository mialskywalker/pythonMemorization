from OOP.classes_and_objects.exercises.library import Library
from OOP.classes_and_objects.exercises.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user_id == user.user_id:
                if new_username != user.username:
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                elif new_username == user.username:
                    return "Please check again the provided username" \
                           " - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
