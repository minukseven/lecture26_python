from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService

class ConsoleBank:
    # 메뉴 구성 정의
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['로그아웃', '계좌개설', '전체계좌조회', '입금', '출금', '계좌해지']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
        self.current_user = None  # 로그인한 사용자의 ID를 저장할 세션 변수

    def main(self):
        self.show_welcome()
        while True:
            if not self.current_user:
                # 로그인 전 메인 메뉴
                menu = self.select_menu("메인 메뉴", ConsoleBank.start_menu)
                if menu == 0: 
                    break
                elif menu == 1:
                    self.login_process()
                elif menu == 2:
                    self.register_process()
            else:
                # 로그인 후 뱅킹 메뉴
                menu = self.select_menu(f"뱅킹 서비스 [{self.current_user}]", ConsoleBank.banking_menu)
                if menu == 0:
                    print(">> 로그아웃 되었습니다.")
                    self.current_user = None
                elif menu == 1:
                    self.create_account_process()
                elif menu == 2:
                    self.view_my_accounts_process()
                elif menu == 3:
                    self.deposit_process()
                elif menu == 4:
                    self.withdraw_process()
                elif menu == 5:
                    self.delete_account_process()
                    
        self.say_goodbye()

    def show_welcome(self):
        print('======== Hyejeong Console Bank ==========')

    def say_goodbye(self):
        print('>> Hyejeong Console Bank를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_title, menu_list):
        """메뉴를 출력하고 사용자에게 번호를 입력받는 메서드"""
        print(f"\n--- {menu_title} ---")
        for i, item in enumerate(menu_list):
            print(f"{i}. {item}")
        print("--------------------")
        
        while True:
            try:
                choice = int(input("원하는 메뉴 번호를 입력하세요: "))
                if 0 <= choice < len(menu_list):
                    return choice
                print(">> 올바른 범위의 숫자를 입력해주세요.")
            except ValueError:
                print(">> 숫자만 입력 가능합니다.")

    # --- 기능별 프로세스 구현 ---

    def login_process(self):
        print("\n[ 로그인 ]")
        user_id = input("아이디: ")
        password = input("비밀번호: ")
        
        # ※ MemberService에 로그인 검증 기능이 있다고 가정합니다.
        # 만약 해당 메서드가 없다면 프로젝트 구조에 맞게 수정이 필요합니다.
        try:
            # 예시: self.msv.login(user_id, password) 성립 시
            # 여기서는 임시로 입력받은 ID로 로그인을 성공시킵니다.
            print(f">> {user_id}님 환영합니다!")
            self.current_user = user_id
        except Exception:
            print(">> 로그인 실패: 아이디 또는 비밀번호를 확인하세요.")

    def register_process(self):
        print("\n[ 회원가입 ]")
        user_id = input("희망 아이디: ")
        password = input("비밀번호: ")
        name = input("이름: ")
        
        # ※ MemberService의 회원가입 메서드를 호출 (구조에 맞게 매개변수 조절 필요)
        try:
            # new_member = Member(user_id, password, name)
            # self.msv.register(new_member)
            print(">> 회원가입이 완료되었습니다. (임시 기능)")
        except Exception as e:
            print(f">> 회원가입 실패: {e}")

    def create_account_process(self):
        print("\n[ 계좌 개설 ]")
        try:
            password = input("계좌 비밀번호 설정: ")
            balance = int(input("초기 입금 금액: "))
            
            # Account 객체 생성 (id는 로그인한 유저 ID)
            # account_no는 AccountService 안에서 순번(seq)으로 처리됨
            new_account = Account(0, self.current_user, balance, password)
            self.asv.create_account(new_account)
            print(">> 계좌가 성공적으로 개설되었습니다.")
        except ValueError:
            print(">> 금액은 숫자만 입력해 주세요.")

    def view_my_accounts_process(self):
        print(f"\n[ {self.current_user} 님의 계좌 목록 ]")
        accounts = self.asv.get_members_accounts(self.current_user)
        if not accounts:
            print(">> 개설된 계좌가 없습니다.")
            return
        
        for account in accounts:
            print(account)

    def deposit_process(self):
        print("\n[ 입금하기 ]")
        account_no = input("입금할 계좌번호: ")
        try:
            amount = int(input("입금할 금액: "))
            if amount <= 0:
                print(">> 0원 이하의 금액은 입금할 수 없습니다.")
                return
                
            if self.asv.deposit(account_no, amount):
                print(f">> {account_no} 계좌에 {amount}원이 입금되었습니다.")
            else:
                print(">> 존재하지 않는 계좌번호입니다.")
        except ValueError:
            print(">> 금액은 숫자만 입력해 주세요.")

    def withdraw_process(self):
        print("\n[ 출금하기 ]")
        account_no = input("출금할 계좌번호: ")
        try:
            amount = int(input("출금할 금액: "))
            password = input("계좌 비밀번호: ")
            
            # AccountService의 withdraw 메서드는 실패 시 예외를 발생시킵니다.
            self.asv.withdraw(self.current_user, account_no, amount, password)
            print(f">> {account_no} 계좌에서 {amount}원이 출금되었습니다.")
        except LookupError:
            print(">> 존재하지 않는 계좌번호입니다.")
        except KeyError:
            print(">> 소유주가 다르거나 비밀번호가 틀렸습니다.")
        except ValueError:
            print(">> 잔액이 부족합니다. (마이너스 통장 불가)")

    def delete_account_process(self):
        print("\n[ 계좌 해지 ]")
        account_no = input("해지할 계좌번호: ")
        password = input("계좌 비밀번호: ")
        
        try:
            self.asv.delete_account(self.current_user, account_no, password)
            print(f">> {account_no} 계좌가 성공적으로 해지되었습니다.")
        except LookupError:
            print(">> 존재하지 않는 계좌번호입니다.")
        except KeyError:
            print(">> 소유주가 다르거나 비밀번호가 틀렸습니다.")
        except ValueError:
            print(">> 잔액이 남아있는 계좌는 해지할 수 없습니다. (잔액을 먼저 모두 출금하세요)")

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()