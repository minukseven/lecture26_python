from Book.book_dao import BookDAO
from Book.book import Book

class BookService:
    def __init__(self, dao):
        self.__dao = dao

    def add_book(self, book):
        return self.__dao.insert_book(book)

    def get_all_books(self):
        return self.__dao.select_all_books()

    def get_book(self, book_no):
        return self.__dao.select_book_by_no(book_no)

    def update_book(self, book_no, book):
        return self.__dao.update_book(book_no, book)

    def delete_book(self, book_no):
        return self.__dao.delete_book(book_no)

    def decrease_stock(self, book_no, amount):
        book = self.__dao.select_book_by_no(book_no)
        if not book:
            raise LookupError
        if book.get_stock() < amount:
            raise ValueError
        book.set_stock(book.get_stock() - amount)
        self.__dao.update_book(book_no, book)

    def restore_stock(self, book_no, amount):
        book = self.__dao.select_book_by_no(book_no)
        if book:
            book.set_stock(book.get_stock() + amount)
            self.__dao.update_book(book_no, book)