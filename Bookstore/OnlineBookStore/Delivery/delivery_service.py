from Delivery.delivery_dao import DeliveryDAO
from Delivery.delivery import Delivery

class DeliveryService:
    def __init__(self, dao):
        self.__dao = dao

    def create_delivery(self, order_no, member_id, address):
        delivery = Delivery(0, order_no, member_id, address)
        return self.__dao.insert_delivery(delivery)

    def get_my_deliveries(self, member_id):
        return self.__dao.select_deliveries_by_member(member_id)

    def get_delivery(self, delivery_no):
        return self.__dao.select_delivery_by_no(delivery_no)

    def get_all_deliveries(self):
        return self.__dao.select_all_deliveries()

    def update_status(self, delivery_no, status):
        delivery = self.__dao.select_delivery_by_no(delivery_no)
        if not delivery:
            raise LookupError
        delivery.set_status(status)
        return self.__dao.update_delivery(delivery_no, delivery)

    def update_address(self, delivery_no, member_id, address):
        delivery = self.__dao.select_delivery_by_no(delivery_no)
        if not delivery:
            raise LookupError
        if delivery.get_member_id() != member_id:
            raise KeyError
        if delivery.get_status() != '배송준비':
            raise ValueError
        delivery.set_address(address)
        return self.__dao.update_delivery(delivery_no, delivery)

    def cancel_delivery(self, delivery_no, member_id):
        delivery = self.__dao.select_delivery_by_no(delivery_no)
        if not delivery:
            raise LookupError
        if delivery.get_member_id() != member_id:
            raise KeyError
        if delivery.get_status() in ('배송완료', '배송취소'):
            raise ValueError
        delivery.set_status('배송취소')
        return self.__dao.update_delivery(delivery_no, delivery)