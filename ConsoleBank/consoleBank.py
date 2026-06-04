from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService
 
 
class ConsoleBank:
    # 메뉴 구성 (인덱스 0 = 종료/로그아웃/돌아가기)
    START_MENU         = ['종료',     '로그인', '회원가입']
    BANKING_MENU       = ['로그아웃', '계좌목록', '입금', '출금', '계좌생성', '계좌해지', '내정보']
    MEMBER_MYINFO_MENU = ['돌아가기', '비밀번호수정', '회원탈퇴']
    ADMIN_MENU         = ['로그아웃', '회원관리', '계좌관리']
    ADMIN_MEMBER_MENU  = ['돌아가기', '회원목록', '회원정보조회', '회원강퇴']
    ADMIN_ACCOUNT_MENU = ['돌아가기', '전체계좌목록', '회원별계좌목록']
 
    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
 
    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()
 
    # ── 메뉴 루프 ──────────────────────────────────────────
    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.START_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_login()
            elif menu == 2: self.menu_join()
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    def run_banking_menu(self):
        self.print_title('회원 메뉴')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(ConsoleBank.BANKING_MENU)
            if menu == 0:   self.menu_logout(); return
            elif menu == 1: self.menu_list_my_accounts()
            elif menu == 2: self.menu_deposit()
            elif menu == 3: self.menu_withdraw()
            elif menu == 4: self.menu_create_account()
            elif menu == 5: self.menu_delete_account()
            elif menu == 6: self.run_my_info_menu()
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    def run_my_info_menu(self):
        self.print_title('내 정보')
        self.menu_view_myinfo()
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(ConsoleBank.MEMBER_MYINFO_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_update_password()
            elif menu == 2: self.menu_delete_membership(); return
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    def run_admin_menu(self):
        self.print_title('관리자 메뉴')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(ConsoleBank.ADMIN_MENU)
            if menu == 0:   self.menu_logout(); return
            elif menu == 1: self.run_admin_member_menu()
            elif menu == 2: self.run_admin_account_menu()
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    def run_admin_member_menu(self):
        self.print_title('회원 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(ConsoleBank.ADMIN_MEMBER_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_list_members()
            elif menu == 2: self.menu_view_member_info()
            elif menu == 3: self.menu_delete_member()
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    def run_admin_account_menu(self):
        self.print_title('계좌 관리')
        while True:
            if self.msv.current_user is None: return
            menu = self.select_menu(ConsoleBank.ADMIN_ACCOUNT_MENU)
            if menu == 0:   return
            elif menu == 1: self.menu_list_all_accounts()
            elif menu == 2: self.menu_list_member_accounts()
            else:           print('[!] 존재하지 않는 메뉴입니다.')
 
    # ── 회원 기능 ──────────────────────────────────────────
    def menu_join(self):
        self.print_title('회원가입')
        id       = input('  아이디   : ')
        password = input('  비밀번호 : ')
        name     = input('  이름     : ')
        if self.msv.join(Member(id, password, name)):
            print('[✓] 회원가입이 완료되었습니다.')
        else:
            print('[!] 이미 사용 중인 아이디입니다.')
 
    def menu_login(self):
        self.print_title('로그인')
        id       = input('  아이디   : ')
        password = input('  비밀번호 : ')
        if self.msv.login(id, password):
            print(f'[✓] {self.msv.view_member_info(id).get_name()}님 환영합니다!')
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_banking_menu()
        else:
            print('[!] 아이디 또는 비밀번호가 올바르지 않습니다.')
 
    def menu_logout(self):
        self.msv.logout()
        print('[✓] 로그아웃 되었습니다.')
 
    # ── 계좌 기능 ──────────────────────────────────────────
    def menu_list_my_accounts(self):
        account_list = self.asv.get_members_accounts(self.msv.current_user)
        print('=' * 40)
        print(f"  {self.msv.current_user} 님의 계좌 목록")
        print('=' * 40)
        if account_list:
            for account in account_list:
                print(' ', account)
        else:
            print('  [!] 개설된 계좌가 없습니다.')
        print('=' * 40)
 
    def menu_deposit(self):
        self.print_title('입금')
        account_no = input('  계좌번호 : ')
        try:
            amount = int(input('  입금금액 : '))
            if amount <= 0:
                print('[!] 0원 이하는 입금할 수 없습니다.')
                return
        except ValueError:
            print('[!] 금액은 숫자만 입력해 주세요.')
            return
        if self.asv.deposit(account_no, amount):
            balance = self.asv.get_account_balance(account_no)
            print(f'[✓] {amount:,}원 입금 완료  |  잔액 : {balance:,}원')
        else:
            print('[!] 존재하지 않는 계좌번호입니다.')
 
    def menu_withdraw(self):
        self.print_title('출금')
        account_no = input('  계좌번호     : ')
        try:
            amount   = int(input('  출금금액     : '))
            password = input('  계좌 비밀번호 : ')
            self.asv.withdraw(self.msv.current_user, account_no, amount, password)
        except LookupError:
            print('[!] 존재하지 않는 계좌번호입니다.')
        except KeyError:
            print('[!] 소유주가 다르거나 비밀번호가 틀렸습니다.')
        except ValueError:
            print('[!] 잔액이 부족합니다.')
        except Exception:
            print('[!] 출금 중 오류가 발생했습니다.')
        else:
            balance = self.asv.get_account_balance(account_no)
            print(f'[✓] {amount:,}원 출금 완료  |  잔액 : {balance:,}원')
 
    def menu_create_account(self):
        self.print_title('계좌 생성')
        try:
            balance = int(input('  초기 예금액       : '))
        except ValueError:
            print('[!] 금액은 숫자만 입력해 주세요.')
            return
        password = input('  계좌 비밀번호 설정 : ')
        if self.asv.create_account(Account(0, self.msv.current_user, balance, password)):
            print('[✓] 계좌가 성공적으로 생성되었습니다.')
        else:
            print('[!] 계좌 생성 중 문제가 발생했습니다.')
 
    def menu_delete_account(self):
        self.print_title('계좌 해지')
        account_no = input('  해지할 계좌번호 : ')
        password   = input('  계좌 비밀번호   : ')
        try:
            self.asv.delete_account(self.msv.current_user, account_no, password)
        except LookupError: print('[!] 존재하지 않는 계좌번호입니다.')
        except KeyError:    print('[!] 소유주가 다르거나 비밀번호가 틀렸습니다.')
        except ValueError:  print('[!] 잔액이 남아 있는 계좌는 해지할 수 없습니다.')
        else:               print('[✓] 계좌가 해지되었습니다.')
 
    # ── 내 정보 기능 ───────────────────────────────────────
    def menu_view_myinfo(self):
        my_info = self.msv.view_member_info(self.msv.current_user)
        if my_info: print(my_info)
        else:       print('[!] 회원 정보를 불러올 수 없습니다.')
 
    def menu_update_password(self):
        self.print_title('비밀번호 수정')
        id           = input('  아이디       : ')
        org_password = input('  현재 비밀번호 : ')
        new_password = input('  새 비밀번호   : ')
        if self.msv.update_member_password(id, org_password, new_password):
            print('[✓] 비밀번호가 변경되었습니다. 다시 로그인해 주세요.')
            self.msv.logout()
        else:
            print('[!] 비밀번호 수정에 실패했습니다.')
 
    def menu_delete_membership(self):
        self.print_title('회원탈퇴')
        confirm = input('  정말 탈퇴하시겠습니까? (yes 입력) : ')
        if confirm.lower() != 'yes':
            print('[!] 탈퇴가 취소되었습니다.')
            return
        account_list = self.asv.get_members_accounts(self.msv.current_user)
        if account_list:
            for account in account_list:
                self.asv.delete_account(account.get_owner(), account.get_account_no(), account.get_password())
        if self.msv.remove_member(self.msv.current_user):
            print('[✓] 회원탈퇴가 완료되었습니다.')
            self.msv.logout()
        else:
            print('[!] 회원탈퇴 중 문제가 발생했습니다.')
 
    # ── 관리자 기능 ────────────────────────────────────────
    def menu_list_members(self):
        members = self.msv.list_members()
        if members:
            print(f'  총 {len(members)}명')
            for member in members: print(' ', member)
        else:
            print('[!] 등록된 회원이 없습니다.')
 
    def menu_view_member_info(self):
        id     = input('  조회할 회원 아이디 : ')
        member = self.msv.view_member_info(id)
        if member: print(member)
        else:      print('[!] 존재하지 않는 회원입니다.')
 
    def menu_delete_member(self):
        id = input('  강퇴할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('[!] 관리자 계정은 강퇴할 수 없습니다.')
            return
        account_list = self.asv.get_members_accounts(id)
        if account_list:
            for account in account_list:
                self.asv.delete_account(account.get_owner(), account.get_account_no(), account.get_password())
        if self.msv.remove_member(id):
            print(f'[✓] {id} 회원이 강퇴되었습니다.')
        else:
            print('[!] 존재하지 않는 회원입니다.')
 
    def menu_list_all_accounts(self):
        all_accounts = self.asv.get_all_accounts()
        if all_accounts:
            print(f'  총 {len(all_accounts)}개')
            for account in all_accounts: print(' ', account)
        else:
            print('[!] 개설된 계좌가 없습니다.')
 
    def menu_list_member_accounts(self):
        id              = input('  조회할 회원 아이디 : ')
        member_accounts = self.asv.get_members_accounts(id)
        if member_accounts:
            for account in member_accounts: print(' ', account)
        else:
            print('[!] 해당 회원의 계좌가 존재하지 않습니다.')
 
    # ── UI 유틸 ────────────────────────────────────────────
    def show_welcome(self):
        self.print_title('Welcome to Console Bank')
 
    def say_goodbye(self):
        print('\n  이용해 주셔서 감사합니다. 안녕히 가세요!\n')
 
    def print_title(self, title):
        print(f"\n{'─' * 44}\n  {title}\n{'─' * 44}")
 
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
    app = ConsoleBank()
    app.main()