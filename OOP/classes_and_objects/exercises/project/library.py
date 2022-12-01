from OOP.classes_and_objects.exercises.project.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available.keys():
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                for k, v in self.books_available.items():
                    if k == author:
                        v.remove(book_name)

                self.rented_books[user.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        return_days = 0
        for k, v in self.rented_books.items():
            if k == user.username:
                for n, value in v.items():
                    if n == book_name:
                        return_days = value

        return f'The book "{book_name}" is already rented and will be available in' \
               f' {return_days} days!'

    def return_book(self, author: str, book_name: str, user: User):

        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        self.books_available[author].append(book_name)
        user.books.remove(book_name)
        for k, v in self.rented_books.items():
            if k == user.username:
                if book_name in v.keys():
                    v.pop(book_name)

# books_available {authors: [books_available]}
# rented_books {username: {book_names: days_left}}
