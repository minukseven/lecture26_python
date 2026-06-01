from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService

class ConsoleBank:
    start_menu         = ['종료', '로그인', '회원가입']
    banking_menu       = ['종료', '잔액조회', '입금', '출금', '이체', '내정보']
    member_myinfo_menu = ['뒤로', '개인정보 수정', '비밀번호 변경', '회원탈퇴']
    admin_menu         = ['종료', '계좌관리', '회원관리']
    admin_account_menu = ['뒤로', '전체계좌조회', '계좌검색', '계좌삭제']
    admin_member_menu  = ['뒤로', '전체회원조회', '회원검색', '회원삭제']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def main(self):
        self.show_welcome()
        while True:
            menu = self.select_menu(ConsoleBank.start_menu)  # ← 버그 수정
            if menu == 0: break
            elif menu == 1: pass   # 추후 login() 연결
            elif menu == 2: pass   # 추후 register() 연결
        self.say_goodbye()

    def show_welcome(self):
        print('======== Hyejeong Console Bank ==========')

    def say_goodbye(self):
        print('>> Hyejeong Console Bank를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print()
        for i, item in enumerate(menu_list):
            print(f'  {i}. {item}')
        while True:
            try:
                choice = int(input(f'메뉴 선택 (0~{len(menu_list)-1}): '))
                if 0 <= choice < len(menu_list):
                    return choice
                print(f'  >> 0~{len(menu_list)-1} 사이의 번호를 입력하세요.')
            except ValueError:
                print('  >> 숫자를 입력하세요.')

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()