from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Product.product import Product
from Product.product_dao import ProductDAO
from Product.product_service import ProductService
from Cart.cart import Item
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_service import OrderService


class SportsShop:
    # 메뉴 구성 (인덱스 0번 = 종료 / 로그아웃 / 돌아가기)
    START_MENU        = ['종료',     '로그인', '회원가입']
    MEMBER_MENU       = ['로그아웃', '상품조회', '장바구니', '주문내역조회', '내정보']
    PRODUCT_MENU      = ['돌아가기', '상품상세보기', '장바구니 추가', '구매하기']
    CART_MENU         = ['돌아가기', '장바구니삭제', '상품상세보기', '구매하기']
    MYORDER_MENU      = ['돌아가기', '주문상세조회', '주문취소']
    MYINFO_MENU       = ['돌아가기', '내정보수정', '회원탈퇴']
    ADMIN_MENU        = ['로그아웃', '상품관리', '회원관리', '주문관리']
    ADMIN_PRODUCT_MENU = ['돌아가기', '상품등록', '상품수정', '상품삭제']
    ADMIN_MEMBER_MENU  = ['돌아가기', '회원목록조회', '회원상세조회', '회원삭제']
    ADMIN_ORDER_MENU   = ['돌아가기', '전체주문조회', '회원별주문조회']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.psv = ProductService(ProductDAO())
        self.csv = CartService(CartDAO())
        self.osv = OrderService(OrderDAO())
        self.init_sample_products()

    def init_sample_products(self):
        self.psv.add_product(Product(0, '런닝화 에어맥스', '신발', '나이키', 129000, 15))
        self.psv.add_product(Product(0, '요가매트 프리미엄', '요가용품', '데카트론', 35000, 30))
        self.psv.add_product(Product(0, '헬스장갑', '헬스용품', '언더아머', 18000, 50))

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    # ===================== 메뉴 루프 =====================

    def run_start_menu(self):
        while True:
            menu = self.select_menu(SportsShop.START_MENU)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
            else:
                print('없는 메뉴입니다.')

    def run_member_menu(self):
        self.print_title('회원메뉴')
        while True:
            if self.msv.current_user is None:
                return
            menu = self.select_menu(SportsShop.MEMBER_MENU)
            if menu == 0:
                self.menu_logout()
                return
            elif menu == 1: self.run_product_menu()
            elif menu == 2: self.run_cart_menu()
            elif menu == 3: self.run_myorder_menu()
            elif menu == 4: self.run_myinfo_menu()
            else:           print('없는 메뉴입니다.')

    def run_product_menu(self):
        self.print_title('상품조회메뉴')
        while True:
            if self.msv.current_user is None:
                return
            self.menu_product_list()
            menu = self.select_menu(SportsShop.PRODUCT_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_product_detail()
            elif menu == 2: self.menu_add_to_cart()
            elif menu == 3: self.menu_buy_now()
            else:           print('없는 메뉴입니다.')

    def run_cart_menu(self):
        self.print_title('장바구니메뉴')
        while True:
            if self.msv.current_user is None:
                return
            self.menu_view_cart()
            menu = self.select_menu(SportsShop.CART_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_delete_cart_item()
            elif menu == 2: self.menu_cart_item_detail()
            elif menu == 3: self.menu_order_from_cart()
            else:           print('없는 메뉴입니다.')

    def run_myorder_menu(self):
        self.print_title('주문내역메뉴')
        while True:
            if self.msv.current_user is None:
                return
            self.menu_my_orders()
            menu = self.select_menu(SportsShop.MYORDER_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_order_detail()
            elif menu == 2: self.menu_cancel_order()
            else:           print('없는 메뉴입니다.')

    def run_myinfo_menu(self):
        self.print_title('내정보메뉴')
        self.menu_view_myinfo()
        while True:
            if self.msv.current_user is None:
                return
            menu = self.select_menu(SportsShop.MYINFO_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_update_myinfo()
            elif menu == 2: self.menu_delete_membership(); return
            else:           print('없는 메뉴입니다.')

    def run_admin_menu(self):
        self.print_title('관리자메뉴')
        while True:
            if self.msv.current_user is None:
                return
            menu = self.select_menu(SportsShop.ADMIN_MENU)
            if menu == 0:
                self.menu_logout()
                return
            elif menu == 1: self.run_admin_product_menu()
            elif menu == 2: self.run_admin_member_menu()
            elif menu == 3: self.run_admin_order_menu()
            else:           print('없는 메뉴입니다.')

    def run_admin_product_menu(self):
        self.print_title('상품관리메뉴')
        while True:
            if self.msv.current_user is None:
                return
            self.menu_product_list()
            menu = self.select_menu(SportsShop.ADMIN_PRODUCT_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_add_product()
            elif menu == 2: self.menu_update_product()
            elif menu == 3: self.menu_delete_product()
            else:           print('없는 메뉴입니다.')

    def run_admin_member_menu(self):
        self.print_title('회원관리메뉴')
        while True:
            if self.msv.current_user is None:
                return
            menu = self.select_menu(SportsShop.ADMIN_MEMBER_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_list_members()
            elif menu == 2: self.menu_view_member_info()
            elif menu == 3: self.menu_delete_member()
            else:           print('없는 메뉴입니다.')

    def run_admin_order_menu(self):
        self.print_title('주문관리메뉴')
        while True:
            if self.msv.current_user is None:
                return
            menu = self.select_menu(SportsShop.ADMIN_ORDER_MENU)
            if menu == 0:
                return
            elif menu == 1: self.menu_list_all_orders()
            elif menu == 2: self.menu_list_member_orders()
            else:           print('없는 메뉴입니다.')

    # ===================== 회원 기능 =====================

    def menu_join(self):
        self.print_title('회원가입')
        id       = input('>> 아이디   : ')
        password = input('>> 비밀번호 : ')
        name     = input('>> 이름     : ')
        if self.msv.join(Member(id, password, name)):
            print('회원가입이 완료되었습니다.')
        else:
            print('이미 사용 중인 아이디입니다.')

    def menu_login(self):
        self.print_title('로그인')
        id       = input('>> 아이디   : ')
        password = input('>> 비밀번호 : ')
        if self.msv.login(id, password):
            name = self.msv.view_member_info(id).get_name()
            print(f'{name}님 환영합니다.')
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_member_menu()
        else:
            print('아이디 또는 비밀번호가 올바르지 않습니다.')

    def menu_logout(self):
        self.msv.logout()
        print('로그아웃 되었습니다.')

    def menu_view_myinfo(self):
        member = self.msv.view_member_info(self.msv.current_user)
        if member:
            print(f'\n  {member}')
        else:
            print('회원 정보를 불러올 수 없습니다.')

    def menu_update_myinfo(self):
        self.print_title('내정보수정')
        org_pw = input('>> 현재 비밀번호 : ')
        new_pw = input('>> 새 비밀번호   : ')
        if self.msv.update_member_password(self.msv.current_user, org_pw, new_pw):
            print('비밀번호가 변경되었습니다. 다시 로그인해 주세요.')
            self.msv.logout()
        else:
            print('비밀번호 수정에 실패했습니다.')

    def menu_delete_membership(self):
        self.print_title('회원탈퇴')
        confirm = input('정말 탈퇴하시겠습니까? (yes 입력) : ')
        if confirm.lower() != 'yes':
            print('취소되었습니다.')
            return
        self.csv.clear_cart(self.msv.current_user)
        if self.msv.remove_member(self.msv.current_user):
            print('회원탈퇴가 완료되었습니다.')
            self.msv.logout()
        else:
            print('회원탈퇴 처리 중 문제가 발생했습니다.')

    # ===================== 상품 기능 =====================

    def menu_product_list(self):
        print('-' * 50)
        print('  상품목록')
        print('-' * 50)
        products = self.psv.get_all_products()
        if products:
            for p in products:
                print(f'  {p}')
        else:
            print('  등록된 상품이 없습니다.')
        print('-' * 50)

    def menu_product_detail(self):
        product_no = input('>> 상품 번호 : ')
        product    = self.psv.get_product(product_no)
        if product:
            print(f'\n  {product}')
        else:
            print('존재하지 않는 상품 번호입니다.')

    def menu_add_to_cart(self):
        product_no = input('>> 담을 상품 번호 : ')
        product    = self.psv.get_product(product_no)
        if not product:
            print('존재하지 않는 상품 번호입니다.')
            return
        try:
            amount = int(input('>> 수량 : '))
            if amount <= 0:
                print('수량은 1 이상이어야 합니다.')
                return
            if amount > product.get_stock():
                print(f'재고가 부족합니다. (현재 재고: {product.get_stock()})')
                return
        except ValueError:
            print('숫자만 입력해 주세요.')
            return
        self.csv.add_item(product_no, self.msv.current_user, amount)
        print('장바구니에 담았습니다.')

    def menu_buy_now(self):
        product_no = input('>> 구매할 상품 번호 : ')
        product    = self.psv.get_product(product_no)
        if not product:
            print('존재하지 않는 상품 번호입니다.')
            return
        try:
            amount = int(input('>> 수량 : '))
            if amount <= 0:
                print('수량은 1 이상이어야 합니다.')
                return
        except ValueError:
            print('숫자만 입력해 주세요.')
            return
        try:
            self.psv.decrease_stock(product_no, amount)
        except ValueError:
            print(f'재고가 부족합니다. (현재 재고: {product.get_stock()})')
            return
        total_price = product.get_price() * amount
        self.osv.create_order(self.msv.current_user, product_no, amount, total_price)
        print(f'주문이 완료되었습니다. (결제금액: {total_price:,}원)')

    # ===================== 장바구니 기능 =====================

    def menu_view_cart(self):
        print('-' * 50)
        print(f'  {self.msv.current_user} 님의 장바구니')
        print('-' * 50)
        items = self.csv.get_my_cart(self.msv.current_user)
        if items:
            total = 0
            for item in items:
                product = self.psv.get_product(item.get_product_no())
                if product:
                    subtotal = product.get_price() * item.get_amount()
                    total   += subtotal
                    print(f'  {item} | 상품명: {product.get_name()} | 소계: {subtotal:,}원')
            print(f'  {"합계":>40} : {total:,}원')
        else:
            print('  장바구니가 비어있습니다.')
        print('-' * 50)

    def menu_delete_cart_item(self):
        item_no = input('>> 삭제할 장바구니 번호 : ')
        try:
            self.csv.delete_item(item_no, self.msv.current_user)
            print('삭제되었습니다.')
        except LookupError:
            print('존재하지 않는 항목입니다.')
        except KeyError:
            print('본인의 장바구니 항목이 아닙니다.')

    def menu_cart_item_detail(self):
        item_no = input('>> 조회할 장바구니 번호 : ')
        item    = self.csv.get_item(item_no)
        if not item:
            print('존재하지 않는 항목입니다.')
            return
        product = self.psv.get_product(item.get_product_no())
        if product:
            print(f'\n  {product}')
        else:
            print('해당 상품 정보를 찾을 수 없습니다.')

    def menu_order_from_cart(self):
        items = self.csv.get_my_cart(self.msv.current_user)
        if not items:
            print('장바구니가 비어있습니다.')
            return
        confirm = input('장바구니 전체를 주문하시겠습니까? (yes 입력) : ')
        if confirm.lower() != 'yes':
            print('주문이 취소되었습니다.')
            return
        for item in items:
            product = self.psv.get_product(item.get_product_no())
            if not product:
                continue
            try:
                self.psv.decrease_stock(item.get_product_no(), item.get_amount())
                total_price = product.get_price() * item.get_amount()
                self.osv.create_order(
                    self.msv.current_user,
                    item.get_product_no(),
                    item.get_amount(),
                    total_price
                )
            except ValueError:
                print(f'{product.get_name()} 재고 부족으로 주문에서 제외됩니다.')
        self.csv.clear_cart(self.msv.current_user)
        print('주문이 완료되었습니다.')

    # ===================== 주문내역 기능 =====================

    def menu_my_orders(self):
        print('-' * 50)
        print('  내 주문내역')
        print('-' * 50)
        orders = self.osv.get_my_orders(self.msv.current_user)
        if orders:
            for order in orders:
                print(f'  {order}')
        else:
            print('  주문 내역이 없습니다.')
        print('-' * 50)

    def menu_order_detail(self):
        order_no = input('>> 조회할 주문번호 : ')
        order    = self.osv.get_order(order_no)
        if not order:
            print('존재하지 않는 주문번호입니다.')
            return
        product = self.psv.get_product(order.get_product_no())
        print(f'\n  {order}')
        if product:
            print(f'  상품명: {product.get_name()}')

    def menu_cancel_order(self):
        order_no = input('>> 취소할 주문번호 : ')
        try:
            cancelled = self.osv.cancel_order(order_no, self.msv.current_user)
            self.psv.restore_stock(cancelled.get_product_no(), cancelled.get_amount())
            print('주문이 취소되었습니다.')
        except LookupError:
            print('존재하지 않는 주문번호입니다.')
        except KeyError:
            print('본인의 주문이 아닙니다.')
        except ValueError:
            print('이미 취소된 주문입니다.')

    # ===================== 관리자 - 상품 기능 =====================

    def menu_add_product(self):
        self.print_title('상품등록')
        name     = input('>> 상품명   : ')
        category = input('>> 카테고리 : ')
        brand    = input('>> 브랜드   : ')
        try:
            price = int(input('>> 가격 : '))
            stock = int(input('>> 재고 : '))
        except ValueError:
            print('가격과 재고는 숫자만 입력해 주세요.')
            return
        product_no = self.psv.add_product(Product(0, name, category, brand, price, stock))
        print(f'상품이 등록되었습니다. (상품번호: {product_no})')

    def menu_update_product(self):
        product_no = input('>> 수정할 상품 번호 : ')
        product    = self.psv.get_product(product_no)
        if not product:
            print('존재하지 않는 상품 번호입니다.')
            return
        print('  (변경하지 않을 항목은 엔터)')
        name     = input(f'>> 상품명   [{product.get_name()}] : ')     or product.get_name()
        category = input(f'>> 카테고리 [{product.get_category()}] : ') or product.get_category()
        brand    = input(f'>> 브랜드   [{product.get_brand()}] : ')    or product.get_brand()
        try:
            price_in = input(f'>> 가격 [{product.get_price()}] : ')
            stock_in = input(f'>> 재고 [{product.get_stock()}] : ')
            price = int(price_in) if price_in else product.get_price()
            stock = int(stock_in) if stock_in else product.get_stock()
        except ValueError:
            print('가격과 재고는 숫자만 입력해 주세요.')
            return
        product.set_name(name)
        product.set_category(category)
        product.set_brand(brand)
        product.set_price(price)
        product.set_stock(stock)
        if self.psv.update_product(product_no, product):
            print('상품 정보가 수정되었습니다.')
        else:
            print('수정에 실패했습니다.')

    def menu_delete_product(self):
        product_no = input('>> 삭제할 상품 번호 : ')
        if self.psv.delete_product(product_no):
            print('상품이 삭제되었습니다.')
        else:
            print('존재하지 않는 상품 번호입니다.')

    # ===================== 관리자 - 회원 기능 =====================

    def menu_list_members(self):
        self.print_title('전체 회원 목록')
        members = self.msv.list_members()
        if members:
            print(f'  총 {len(members)}명')
            for m in members:
                print(f'  {m}')
        else:
            print('등록된 회원이 없습니다.')

    def menu_view_member_info(self):
        id     = input('>> 조회할 회원 아이디 : ')
        member = self.msv.view_member_info(id)
        if member:
            print(f'  {member}')
        else:
            print('존재하지 않는 회원입니다.')

    def menu_delete_member(self):
        id = input('>> 삭제할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('관리자 계정은 삭제할 수 없습니다.')
            return
        self.csv.clear_cart(id)
        if self.msv.remove_member(id):
            print(f'{id} 회원이 삭제되었습니다.')
        else:
            print('존재하지 않는 회원입니다.')

    # ===================== 관리자 - 주문 기능 =====================

    def menu_list_all_orders(self):
        self.print_title('전체 주문 목록')
        orders = self.osv.get_all_orders()
        if orders:
            print(f'  총 {len(orders)}건')
            for o in orders:
                print(f'  회원: {o.get_member_id()} | {o}')
        else:
            print('주문 내역이 없습니다.')

    def menu_list_member_orders(self):
        id     = input('>> 조회할 회원 아이디 : ')
        orders = self.osv.get_my_orders(id)
        if orders:
            for o in orders:
                print(f'  {o}')
        else:
            print('해당 회원의 주문 내역이 없습니다.')

    # ===================== UI 유틸 =====================

    def show_welcome(self):
        print('=' * 50)
        title = 'Sports Goods Shop'
        print(f'{title:^50}')
        print('=' * 50)

    def say_goodbye(self):
        print('\n이용해 주셔서 감사합니다. 안녕히 가세요!\n')

    def print_title(self, title):
        print(f'\n---------- {title} ----------')

    def select_menu(self, menu_list):
        print('-' * 40)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 40)
        try:
            return int(input('메뉴 선택 : '))
        except ValueError:
            return -1


if __name__ == '__main__':
    app = SportsShop()
    app.main()
