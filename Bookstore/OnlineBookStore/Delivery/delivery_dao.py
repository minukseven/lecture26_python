from Delivery.delivery import Delivery

class DeliveryDAO:
    def __init__(self):
        self.__deliveryDB = {}
        self.__seq        = 1

    def insert_delivery(self, delivery):
        delivery_no = str(self.__seq)
        self.__seq += 1
        new_delivery = Delivery(
            delivery_no,
            delivery.get_order_no(),
            delivery.get_member_id(),
            delivery.get_address()
        )
        self.__deliveryDB[delivery_no] = new_delivery
        return delivery_no

    def select_delivery_by_no(self, delivery_no):
        return self.__deliveryDB.get(delivery_no, None)

    def select_deliveries_by_member(self, member_id):
        result = [d for d in self.__deliveryDB.values() if d.get_member_id() == member_id]
        return result if result else None

    def select_all_deliveries(self):
        return list(self.__deliveryDB.values()) if self.__deliveryDB else None

    def update_delivery(self, delivery_no, delivery):
        if delivery_no in self.__deliveryDB:
            self.__deliveryDB[delivery_no] = delivery
            return True
        return False

    def delete_delivery(self, delivery_no):
        if delivery_no in self.__deliveryDB:
            del self.__deliveryDB[delivery_no]
            return True
        return False