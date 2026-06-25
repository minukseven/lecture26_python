from Product.product_dao import ProductDAO

class ProductService:
    def __init__(self, dao):
        self.__dao = dao

    def add_product(self, product):
        return self.__dao.insert_product(product)

    def get_all_products(self):
        return self.__dao.select_all_products()

    def get_product(self, product_no):
        return self.__dao.select_product_by_no(product_no)

    def update_product(self, product_no, product):
        return self.__dao.update_product(product_no, product)

    def delete_product(self, product_no):
        return self.__dao.delete_product(product_no)

    def decrease_stock(self, product_no, amount):
        product = self.__dao.select_product_by_no(product_no)
        if not product:
            raise LookupError
        if product.get_stock() < amount:
            raise ValueError
        product.set_stock(product.get_stock() - amount)
        self.__dao.update_product(product_no, product)

    def restore_stock(self, product_no, amount):
        product = self.__dao.select_product_by_no(product_no)
        if product:
            product.set_stock(product.get_stock() + amount)
            self.__dao.update_product(product_no, product)
