from Product.product import Product

class ProductDAO:
    def __init__(self):
        self.__productDB = {}
        self.__seq       = 1

    def insert_product(self, product):
        product_no = str(self.__seq)
        self.__seq += 1
        self.__productDB[product_no] = Product(
            product_no,
            product.get_name(), product.get_category(),
            product.get_brand(), product.get_price(), product.get_stock()
        )
        return product_no

    def select_product_by_no(self, product_no):
        return self.__productDB.get(product_no, None)

    def select_all_products(self):
        return list(self.__productDB.values()) if self.__productDB else None

    def update_product(self, product_no, product):
        if product_no in self.__productDB:
            self.__productDB[product_no] = product
            return True
        return False

    def delete_product(self, product_no):
        if product_no in self.__productDB:
            del self.__productDB[product_no]
            return True
        return False
