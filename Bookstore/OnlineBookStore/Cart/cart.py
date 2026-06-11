class Item:
    def __init__(self, item_no, book_no, member_id, amount):
        self.__item_no   = item_no
        self.__book_no   = book_no
        self.__member_id = member_id
        self.__amount    = amount

    def get_item_no(self):   return self.__item_no
    def get_book_no(self):   return self.__book_no
    def get_member_id(self): return self.__member_id
    def get_amount(self):    return self.__amount

    def set_amount(self, amount): self.__amount = amount

    def __str__(self):
        return (f'장바구니번호: {self.__item_no} | '
                f'책번호: {self.__book_no} | 수량: {self.__amount}')