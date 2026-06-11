from Book.book import Book

class BookDAO:
    def __init__(self):
        self.__bookDB = {}
        self.__seq    = 1

    def insert_book(self, book):
        book_no = str(self.__seq)
        self.__seq += 1
        self.__bookDB[book_no] = Book(
            book_no,
            book.get_title(), book.get_author(),
            book.get_publisher(), book.get_price(), book.get_stock()
        )
        return book_no

    def select_book_by_no(self, book_no):
        return self.__bookDB.get(book_no, None)

    def select_all_books(self):
        return list(self.__bookDB.values()) if self.__bookDB else None

    def update_book(self, book_no, book):
        if book_no in self.__bookDB:
            self.__bookDB[book_no] = book
            return True
        return False

    def delete_book(self, book_no):
        if book_no in self.__bookDB:
            del self.__bookDB[book_no]
            return True
        return False