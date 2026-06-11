from Order.order import Order

class OrderDAO:
    def __init__(self):
        self.__orderDB = {}
        self.__seq     = 1

    def insert_order(self, order):
        order_no = str(self.__seq)
        self.__seq += 1
        new_order = Order(order_no, order.get_member_id(), order.get_book_no(),
                          order.get_amount(), order.get_total_price())
        self.__orderDB[order_no] = new_order
        return order_no

    def select_order_by_no(self, order_no):
        return self.__orderDB.get(order_no, None)

    def select_orders_by_member(self, member_id):
        result = [o for o in self.__orderDB.values() if o.get_member_id() == member_id]
        return result if result else None

    def select_all_orders(self):
        return list(self.__orderDB.values()) if self.__orderDB else None

    def update_order(self, order_no, order):
        if order_no in self.__orderDB:
            self.__orderDB[order_no] = order
            return True
        return False

    def delete_order(self, order_no):
        if order_no in self.__orderDB:
            del self.__orderDB[order_no]
            return True
        return False