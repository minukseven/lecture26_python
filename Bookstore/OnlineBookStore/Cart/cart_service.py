from Cart.cart_dao import CartDAO
from Cart.cart import Item

class CartService:
    def __init__(self, dao):
        self.__dao = dao

    def add_item(self, book_no, member_id, amount):
        item = Item(0, book_no, member_id, amount)
        return self.__dao.insert_item(item)

    def get_my_cart(self, member_id):
        return self.__dao.select_items_by_member(member_id)

    def delete_item(self, item_no, member_id):
        item = self.__dao.select_item_by_no(item_no)
        if not item:
            raise LookupError
        if item.get_member_id() != member_id:
            raise KeyError
        return self.__dao.delete_item(item_no)

    def clear_cart(self, member_id):
        self.__dao.delete_items_by_member(member_id)

    def get_item(self, item_no):
        return self.__dao.select_item_by_no(item_no)