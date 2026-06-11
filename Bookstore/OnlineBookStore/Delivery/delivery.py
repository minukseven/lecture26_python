class Delivery:
    def __init__(self, delivery_no, order_no, member_id, address, status='배송준비'):
        self.__delivery_no = delivery_no
        self.__order_no    = order_no
        self.__member_id   = member_id
        self.__address     = address
        self.__status      = status  # 배송준비 / 배송중 / 배송완료 / 배송취소

    def get_delivery_no(self): return self.__delivery_no
    def get_order_no(self):    return self.__order_no
    def get_member_id(self):   return self.__member_id
    def get_address(self):     return self.__address
    def get_status(self):      return self.__status

    def set_address(self, address): self.__address = address
    def set_status(self, status):   self.__status = status

    def __str__(self):
        return (f'배송번호: {self.__delivery_no} | 주문번호: {self.__order_no} | '
                f'주소: {self.__address} | 상태: {self.__status}')