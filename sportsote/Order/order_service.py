from Order.order_dao import OrderDAO
from Order.order import Order

class OrderService:
    def __init__(self, dao):
        self.__dao = dao

    def create_order(self, member_id, book_no, amount, total_price):
        order = Order(0, member_id, book_no, amount, total_price)
        return self.__dao.insert_order(order)

    def get_my_orders(self, member_id):
        return self.__dao.select_orders_by_member(member_id)

    def get_order(self, order_no):
        return self.__dao.select_order_by_no(order_no)

    def get_all_orders(self):
        return self.__dao.select_all_orders()

    def cancel_order(self, order_no, member_id):
        order = self.__dao.select_order_by_no(order_no)
        if not order:
            raise LookupError
        if order.get_member_id() != member_id:
            raise KeyError
        if order.get_status() == '취소':
            raise ValueError
        order.set_status('취소')
        self.__dao.update_order(order_no, order)
        return order  # 재고 복구를 위해 반환

    def update_order(self, order_no, member_id, amount, total_price):
        order = self.__dao.select_order_by_no(order_no)
        if not order:
            raise LookupError
        if order.get_member_id() != member_id:
            raise KeyError
        if order.get_status() == '취소':
            raise ValueError
        order.set_amount(amount)
        order.set_total_price(total_price)
        self.__dao.update_order(order_no, order)
        return order
