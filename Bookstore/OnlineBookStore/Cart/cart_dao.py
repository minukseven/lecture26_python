from Cart.cart import Item

class CartDAO:
    def __init__(self):
        self.__cartDB = {}
        self.__seq    = 1

    def insert_item(self, item):
        item_no = str(self.__seq)
        self.__seq += 1
        new_item = Item(item_no, item.get_book_no(), item.get_member_id(), item.get_amount())
        self.__cartDB[item_no] = new_item
        return item_no

    def select_item_by_no(self, item_no):
        return self.__cartDB.get(item_no, None)

    def select_items_by_member(self, member_id):
        result = [i for i in self.__cartDB.values() if i.get_member_id() == member_id]
        return result if result else None

    def update_item(self, item_no, item):
        if item_no in self.__cartDB:
            self.__cartDB[item_no] = item
            return True
        return False

    def delete_item(self, item_no):
        if item_no in self.__cartDB:
            del self.__cartDB[item_no]
            return True
        return False

    def delete_items_by_member(self, member_id):
        keys = [k for k, v in self.__cartDB.items() if v.get_member_id() == member_id]
        for k in keys:
            del self.__cartDB[k]