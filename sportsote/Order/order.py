class Order:
    def __init__(self, order_no, member_id, book_no, amount, total_price):
        self.__order_no    = order_no
        self.__member_id   = member_id
        self.__book_no     = book_no
        self.__amount      = amount
        self.__total_price = total_price
        self.__status      = '주문완료'  # 주문완료 / 취소

    def get_order_no(self):    return self.__order_no
    def get_member_id(self):   return self.__member_id
    def get_book_no(self):     return self.__book_no
    def get_amount(self):      return self.__amount
    def get_total_price(self): return self.__total_price
    def get_status(self):      return self.__status

    def set_amount(self, v):      self.__amount = v
    def set_total_price(self, v): self.__total_price = v
    def set_status(self, v):      self.__status = v

    def __str__(self):
        return (f'주문번호: {self.__order_no} | 책번호: {self.__book_no} | '
                f'수량: {self.__amount} | 금액: {self.__total_price:,}원 | '
                f'상태: {self.__status}')
