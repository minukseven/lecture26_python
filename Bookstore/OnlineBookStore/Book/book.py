class Book:
    def __init__(self, book_no, title, author, publisher, price, stock):
        self.__book_no   = book_no
        self.__title     = title
        self.__author    = author
        self.__publisher = publisher
        self.__price     = price
        self.__stock     = stock

    def get_book_no(self):   return self.__book_no
    def get_title(self):     return self.__title
    def get_author(self):    return self.__author
    def get_publisher(self): return self.__publisher
    def get_price(self):     return self.__price
    def get_stock(self):     return self.__stock

    def set_title(self, v):     self.__title = v
    def set_author(self, v):    self.__author = v
    def set_publisher(self, v): self.__publisher = v
    def set_price(self, v):     self.__price = v
    def set_stock(self, v):     self.__stock = v

    def __str__(self):
        return (f'[{self.__book_no}] {self.__title} | '
                f'저자: {self.__author} | 출판사: {self.__publisher} | '
                f'가격: {self.__price:,}원 | 재고: {self.__stock}')