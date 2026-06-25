class Product:
    def __init__(self, product_no, name, category, brand, price, stock):
        self.__product_no = product_no
        self.__name       = name
        self.__category   = category
        self.__brand      = brand
        self.__price      = price
        self.__stock      = stock

    def get_product_no(self): return self.__product_no
    def get_name(self):       return self.__name
    def get_category(self):   return self.__category
    def get_brand(self):      return self.__brand
    def get_price(self):      return self.__price
    def get_stock(self):      return self.__stock

    def set_name(self, v):     self.__name = v
    def set_category(self, v): self.__category = v
    def set_brand(self, v):    self.__brand = v
    def set_price(self, v):    self.__price = v
    def set_stock(self, v):    self.__stock = v

    def __str__(self):
        return (f'[{self.__product_no}] {self.__name} | '
                f'카테고리: {self.__category} | 브랜드: {self.__brand} | '
                f'가격: {self.__price:,}원 | 재고: {self.__stock}')
