from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Book.book import Book
from Book.book_dao import BookDAO
from Book.book_service import BookService
from Cart.cart import Item
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_service import OrderService
from Delivery.delivery import Delivery
from Delivery.delivery_dao import DeliveryDAO
from Delivery.delivery_service import DeliveryService


class OnlineBookStore:
    # 메뉴 구성 (인덱스 0 = 종료/로그아웃/돌아가기)
    START_MENU         = ['종료',     '로그인', '회원가입']
    MEMBER_MENU        = ['로그아웃', '장바구니', '주문조회', '배송조회', '내정보', '책목록조회', '책상세조회']
    MYINFO_MENU        = ['돌아가기', '회원정보조회', '회원수정', '회원탈퇴']
    ADMIN_MENU         = ['로그아웃', '회원관리', '책관리', '주문관리', '배송관리']
    ADMIN_MEMBER_MENU  = ['돌아가기', '회원목록조회', '회원상세조회', '회원삭제']
    ADMIN_BOOK_MENU    = ['돌아가기', '책추가', '책수정', '책삭제', '책목록조회']
    ADMIN_ORDER_MENU   = ['돌아가기', '주문목록조회', '회원별주문조회', '주문삭제', '주문수정']
    ADMIN_DELIVERY_MENU = ['돌아가기', '전체배송목록', '배송상태변경', '배송삭제']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.bsv = BookService(BookDAO())
        self.csv = CartService(CartDAO())
        self.osv = OrderService(OrderDAO())
        self.dsv = DeliveryService(DeliveryDAO())
        self._load_sample_books()

    def _load_sample_books(self):
        # 테스트용 샘플 책 데이터
        self.bsv.add_book(Book(0, '파이썬 기초', '홍길동', '한빛미디어', 25000, 10))
        self.bsv.add_book(Book(0, '자바의 정석', '남궁성', 'Do it!', 35000, 5))
        self.bsv.add_book(Book(0, 'SQL 완전정복', '김은아교수님', '성남출판', 28000, 8))

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    # ── 메뉴 루프 ──────────────────────────────────────────
    def run_start_menu(self):
        while True:
            menu = self.select_menu(OnlineBookStore.START_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_login()
            elif menu == 2: self.menu_join()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_member_menu(self):
        self.print_title('회원 메뉴')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.MEMBER_MENU)
            if menu == 0:   self.menu_logout(); return
            elif menu == 1: self.run_cart_menu()
            elif menu == 2: self.menu_my_orders()
            elif menu == 3: self.menu_my_delivery()
            elif menu == 4: self.run_myinfo_menu()
            elif menu == 5: self.menu_book_list()
            elif menu == 6: self.menu_book_detail()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_cart_menu(self):
        self.print_title('장바구니')
        while True:
            if self.msv.current_user is None: return
            self.menu_view_cart()
            print('\n  1. 책 담기  2. 장바구니 삭제  3. 주문하기  0. 돌아가기')
            try:
                menu = int(input('  메뉴 선택 > '))
            except ValueError:
                menu = -1
            if menu == 0:   return
            elif menu == 1: self.menu_add_to_cart()
            elif menu == 2: self.menu_delete_cart_item()
            elif menu == 3: self.menu_order_from_cart()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_myinfo_menu(self):
        self.print_title('내 정보')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.MYINFO_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_view_myinfo()
            elif menu == 2: self.menu_update_myinfo()
            elif menu == 3: self.menu_delete_membership(); return
            else:           print('존재하지 않는 메뉴입니다.')

    def run_admin_menu(self):
        self.print_title('관리자 메뉴')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.ADMIN_MENU)
            if menu == 0:   self.menu_logout(); return
            elif menu == 1: self.run_admin_member_menu()
            elif menu == 2: self.run_admin_book_menu()
            elif menu == 3: self.run_admin_order_menu()
            elif menu == 4: self.run_admin_delivery_menu()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_admin_member_menu(self):
        self.print_title('회원 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.ADMIN_MEMBER_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_list_members()
            elif menu == 2: self.menu_view_member_info()
            elif menu == 3: self.menu_delete_member()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_admin_book_menu(self):
        self.print_title('책 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.ADMIN_BOOK_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_add_book()
            elif menu == 2: self.menu_update_book()
            elif menu == 3: self.menu_delete_book()
            elif menu == 4: self.menu_book_list()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_admin_order_menu(self):
        self.print_title('주문 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.ADMIN_ORDER_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_list_all_orders()
            elif menu == 2: self.menu_list_member_orders()
            elif menu == 3: self.menu_admin_cancel_order()
            elif menu == 4: self.menu_admin_update_order()
            else:           print('존재하지 않는 메뉴입니다.')

    def run_admin_delivery_menu(self):
        self.print_title('배송 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(OnlineBookStore.ADMIN_DELIVERY_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_list_all_deliveries()
            elif menu == 2: self.menu_update_delivery_status()
            elif menu == 3: self.menu_delete_delivery()
            else:           print('존재하지 않는 메뉴입니다.')


    def menu_join(self):
        self.print_title('회원가입')
        id       = input('  아이디   : ')
        password = input('  비밀번호 : ')
        name     = input('  이름     : ')
        if self.msv.join(Member(id, password, name)):
            print('회원가입이 완료되었습니다.')
        else:
            print('이미 사용 중인 아이디입니다.')

    def menu_login(self):
        self.print_title('로그인')
        id       = input('  아이디   : ')
        password = input('  비밀번호 : ')
        if self.msv.login(id, password):
            name = self.msv.view_member_info(id).get_name()
            print(f'{name}님 환영합니다!')
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
        if member: print(f'\n  {member}')
        else:      print('회원 정보를 불러올 수 없습니다.')

    def menu_update_myinfo(self):
        self.print_title('회원 수정')
        org_pw = input('  현재 비밀번호 : ')
        new_pw = input('  새 비밀번호   : ')
        if self.msv.update_member_password(self.msv.current_user, org_pw, new_pw):
            print('비밀번호가 변경되었습니다. 다시 로그인해 주세요.')
            self.msv.logout()
        else:
            print('비밀번호 수정에 실패했습니다.')

    def menu_delete_membership(self):
        self.print_title('회원탈퇴')
        confirm = input('  정말 탈퇴하시겠습니까? (yes 입력) : ')
        if confirm.lower() != 'yes':
            print('취소되었습니다.')
            return
        self.csv.clear_cart(self.msv.current_user)
        if self.msv.remove_member(self.msv.current_user):
            print('회원탈퇴가 완료되었습니다.')
            self.msv.logout()
        else:
            print('회원탈퇴 중 문제가 발생했습니다.')

    # ── 책 기능 ────────────────────────────────────────────
    def menu_book_list(self):
        self.print_title('책 목록')
        books = self.bsv.get_all_books()
        if books:
            for book in books: print(f'  {book}')
        else:
            print('  등록된 책이 없습니다.')

    def menu_book_detail(self):
        self.print_title('책 상세조회')
        book_no = input('  책 번호 : ')
        book    = self.bsv.get_book(book_no)
        if book: print(f'\n  {book}')
        else:    print('존재하지 않는 책 번호입니다.')

    # ── 장바구니 기능 ──────────────────────────────────────
    def menu_view_cart(self):
        print('=' * 50)
        print(f"  {self.msv.current_user} 님의 장바구니")
        print('=' * 50)
        items = self.csv.get_my_cart(self.msv.current_user)
        if items:
            total = 0
            for item in items:
                book = self.bsv.get_book(item.get_book_no())
                if book:
                    subtotal = book.get_price() * item.get_amount()
                    total   += subtotal
                    print(f'  {item} | 책명: {book.get_title()} | 소계: {subtotal:,}원')
            print(f'  {"합계":>40} : {total:,}원')
        else:
            print('  장바구니가 비어있습니다.')
        print('=' * 50)

    def menu_add_to_cart(self):
        self.menu_book_list()
        book_no = input('  담을 책 번호 : ')
        book    = self.bsv.get_book(book_no)
        if not book:
            print('존재하지 않는 책 번호입니다.')
            return
        try:
            amount = int(input('  수량 : '))
            if amount <= 0:
                print('수량은 1 이상이어야 합니다.')
                return
            if amount > book.get_stock():
                print(f'재고가 부족합니다. (현재 재고: {book.get_stock()})')
                return
        except ValueError:
            print('숫자만 입력해 주세요.')
            return
        self.csv.add_item(book_no, self.msv.current_user, amount)
        print('장바구니에 담았습니다.')

    def menu_delete_cart_item(self):
        item_no = input('  삭제할 장바구니 번호 : ')
        try:
            self.csv.delete_item(item_no, self.msv.current_user)
            print('삭제되었습니다.')
        except LookupError: print('존재하지 않는 항목입니다.')
        except KeyError:    print('본인의 장바구니 항목이 아닙니다.')

    def menu_order_from_cart(self):
        items = self.csv.get_my_cart(self.msv.current_user)
        if not items:
            print('장바구니가 비어있습니다.')
            return
        confirm = input('  장바구니 전체를 주문하시겠습니까? (yes 입력) : ')
        if confirm.lower() != 'yes':
            print('주문이 취소되었습니다.')
            return
        address = input('  배송지 주소 : ')
        for item in items:
            book = self.bsv.get_book(item.get_book_no())
            if not book:
                continue
            try:
                self.bsv.decrease_stock(item.get_book_no(), item.get_amount())
                total_price = book.get_price() * item.get_amount()
                order_no = self.osv.create_order(
                    self.msv.current_user,
                    item.get_book_no(),
                    item.get_amount(),
                    total_price
                )
                # 주문 생성과 동시에 배송 정보 생성
                self.dsv.create_delivery(order_no, self.msv.current_user, address)
            except ValueError:
                print(f'{book.get_title()} 재고 부족으로 주문에서 제외됩니다.')
        self.csv.clear_cart(self.msv.current_user)
        print('주문 및 배송 등록이 완료되었습니다.')

    # ── 주문 기능 ──────────────────────────────────────────
    def menu_my_orders(self):
        self.print_title('내 주문 목록')
        orders = self.osv.get_my_orders(self.msv.current_user)
        if orders:
            for order in orders: print(f'  {order}')
        else:
            print('  주문 내역이 없습니다.')

    def menu_my_delivery(self):
        self.print_title('배송 조회')
        deliveries = self.dsv.get_my_deliveries(self.msv.current_user)
        if deliveries:
            for d in deliveries: print(f'  {d}')
        else:
            print('  배송 내역이 없습니다.')

    # ── 관리자 - 회원 기능 ─────────────────────────────────
    def menu_list_members(self):
        members = self.msv.list_members()
        if members:
            print(f'\n  총 {len(members)}명')
            for m in members: print(f'  {m}')
        else:
            print('등록된 회원이 없습니다.')

    def menu_view_member_info(self):
        id     = input('  조회할 회원 아이디 : ')
        member = self.msv.view_member_info(id)
        if member: print(f'  {member}')
        else:      print('존재하지 않는 회원입니다.')

    def menu_delete_member(self):
        id = input('  삭제할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('관리자 계정은 삭제할 수 없습니다.')
            return
        self.csv.clear_cart(id)
        if self.msv.remove_member(id):
            print(f'{id} 회원이 삭제되었습니다.')
        else:
            print('존재하지 않는 회원입니다.')

    # ── 관리자 - 책 기능 ───────────────────────────────────
    def menu_add_book(self):
        self.print_title('책 추가')
        title     = input('  제목    : ')
        author    = input('  저자    : ')
        publisher = input('  출판사  : ')
        try:
            price = int(input('  가격    : '))
            stock = int(input('  재고    : '))
        except ValueError:
            print('가격과 재고는 숫자만 입력해 주세요.')
            return
        book_no = self.bsv.add_book(Book(0, title, author, publisher, price, stock))
        print(f'책이 추가되었습니다. (책번호: {book_no})')

    def menu_update_book(self):
        self.print_title('책 수정')
        self.menu_book_list()
        book_no = input('  수정할 책 번호 : ')
        book    = self.bsv.get_book(book_no)
        if not book:
            print('존재하지 않는 책 번호입니다.')
            return
        print('  (변경하지 않을 항목은 엔터)')
        title     = input(f'  제목 [{book.get_title()}] : ')     or book.get_title()
        author    = input(f'  저자 [{book.get_author()}] : ')    or book.get_author()
        publisher = input(f'  출판사 [{book.get_publisher()}] :') or book.get_publisher()
        try:
            price_in = input(f'  가격 [{book.get_price()}] : ')
            stock_in = input(f'  재고 [{book.get_stock()}] : ')
            price = int(price_in) if price_in else book.get_price()
            stock = int(stock_in) if stock_in else book.get_stock()
        except ValueError:
            print('가격과 재고는 숫자만 입력해 주세요.')
            return
        book.set_title(title); book.set_author(author)
        book.set_publisher(publisher); book.set_price(price); book.set_stock(stock)
        if self.bsv.update_book(book_no, book):
            print('책 정보가 수정되었습니다.')
        else:
            print('수정에 실패했습니다.')

    def menu_delete_book(self):
        self.menu_book_list()
        book_no = input('  삭제할 책 번호 : ')
        if self.bsv.delete_book(book_no):
            print('책이 삭제되었습니다.')
        else:
            print('존재하지 않는 책 번호입니다.')

    # ── 관리자 - 주문 기능 ─────────────────────────────────
    def menu_list_all_orders(self):
        orders = self.osv.get_all_orders()
        if orders:
            print(f'\n  총 {len(orders)}건')
            for o in orders: print(f'  회원: {o.get_member_id()} | {o}')
        else:
            print('주문 내역이 없습니다.')

    def menu_list_member_orders(self):
        id     = input('  조회할 회원 아이디 : ')
        orders = self.osv.get_my_orders(id)
        if orders:
            for o in orders: print(f'  {o}')
        else:
            print('해당 회원의 주문 내역이 없습니다.')

    def menu_admin_cancel_order(self):
        order_no = input('  취소할 주문번호 : ')
        order    = self.osv.get_order(order_no)
        if not order:
            print('존재하지 않는 주문번호입니다.')
            return
        try:
            cancelled = self.osv.cancel_order(order_no, order.get_member_id())
            self.bsv.restore_stock(cancelled.get_book_no(), cancelled.get_amount())
            print('주문이 취소되었습니다.')
        except ValueError: print('이미 취소된 주문입니다.')

    def menu_admin_update_order(self):
        order_no = input('  수정할 주문번호 : ')
        order    = self.osv.get_order(order_no)
        if not order:
            print('존재하지 않는 주문번호입니다.')
            return
        book = self.bsv.get_book(order.get_book_no())
        if not book:
            print('해당 책 정보를 찾을 수 없습니다.')
            return
        try:
            amount      = int(input(f'  수량 [{order.get_amount()}] : '))
            total_price = book.get_price() * amount
            self.bsv.restore_stock(order.get_book_no(), order.get_amount())
            self.bsv.decrease_stock(order.get_book_no(), amount)
            self.osv.update_order(order_no, order.get_member_id(), amount, total_price)
            print('주문이 수정되었습니다.')
        except ValueError:  print('재고가 부족하거나 취소된 주문입니다.')
        except Exception:   print('수정 중 오류가 발생했습니다.')

    # ── 관리자 - 배송 기능 ─────────────────────────────────
    def menu_list_all_deliveries(self):
        deliveries = self.dsv.get_all_deliveries()
        if deliveries:
            print(f'\n  총 {len(deliveries)}건')
            for d in deliveries: print(f'  회원: {d.get_member_id()} | {d}')
        else:
            print('배송 내역이 없습니다.')

    def menu_update_delivery_status(self):
        delivery_no = input('  배송번호 : ')
        print('  상태 선택: 1.배송준비  2.배송중  3.배송완료  4.배송취소')
        status_map  = {'1': '배송준비', '2': '배송중', '3': '배송완료', '4': '배송취소'}
        choice      = input('  선택 > ')
        status      = status_map.get(choice)
        if not status:
            print('올바른 번호를 입력해 주세요.')
            return
        try:
            self.dsv.update_status(delivery_no, status)
            print(f'배송 상태가 [{status}](으)로 변경되었습니다.')
        except LookupError:
            print('존재하지 않는 배송번호입니다.')

    def menu_delete_delivery(self):
        delivery_no = input('  삭제할 배송번호 : ')
        delivery    = self.dsv.get_delivery(delivery_no)
        if not delivery:
            print('존재하지 않는 배송번호입니다.')
            return
        try:
            self.dsv.update_status(delivery_no, '배송취소')
            print('배송이 취소되었습니다.')
        except LookupError:
            print('존재하지 않는 배송번호입니다.')

    # ── UI 유틸 ────────────────────────────────────────────
    def show_welcome(self):
        self.print_title('Welcome to Online Book Store')

    def say_goodbye(self):
        print('\n  이용해 주셔서 감사합니다. 안녕히 가세요!\n')

    def print_title(self, title):
        print(f"\n{'─' * 50}\n  {title}\n{'─' * 50}")

    def select_menu(self, menu_list):
        print()
        for i in range(1, len(menu_list)):
            print(f'  {i}. {menu_list[i]}')
        print(f'  0. {menu_list[0]}')
        print()
        try:
            return int(input('  메뉴 선택 > '))
        except ValueError:
            return -1


if __name__ == '__main__':
    app = OnlineBookStore()
    app.main()