class Member:
    def __init__(self, user_no, user_id, pw, name, phone, address):
        self.__user_no = user_no
        self.__id = user_id
        self.__pw = pw
        self.__name = name
        self.__phone = phone
        self.__address = address

    def get_user_no(self): return self.__user_no
    def get_id(self): return self.__id
    def get_pw(self): return self.__pw
    def get_name(self): return self.__name
    def get_phone(self): return self.__phone
    def get_address(self): return self.__address

    def member_update(self, name, pw, phone, address):
        self.__name = name
        self.__pw = pw
        self.__phone = phone
        self.__address = address

    def __str__(self):
        return (
            f'----------------------\n'
            f'회원번호: {self.__user_no}\n'
            f'아이디  : {self.__id}\n'
            f'이름    : {self.__name}\n'
            f'전화번호: {self.__phone}\n'
            f'주소    : {self.__address}'
        )


class MemberService:
    def __init__(self):
        self.__member_list = []

    # 아이디 중복 확인
    def is_duplicate_id(self, user_id):
        for member in self.__member_list:
            if member.get_id() == user_id:
                return True
        return False

    # 회원가입
    def register_member(self, user_no, user_id, pw, name, phone, address):
        member = Member(user_no, user_id, pw, name, phone, address)
        self.__member_list.append(member)
        return True

    # 회원목록
    def member_list(self):
        return self.__member_list

    # 회원상세정보 (아이디로 조회)
    def info_member_by_id(self, user_id):
        for member in self.__member_list:
            if member.get_id() == user_id:
                return member
        return None

    # 회원정보수정
    def edit_member(self, user_id, pw, name, new_pw, phone, address):
        for member in self.__member_list:
            if member.get_id() == user_id:
                if member.get_pw() != pw:
                    return False
                member.member_update(name, new_pw, phone, address)
                return True
        return False

    # 회원탈퇴
    def del_member(self, user_id, pw):
        for member in self.__member_list:
            if member.get_id() == user_id:
                if member.get_pw() != pw:
                    return False
                self.__member_list.remove(member)
                return True
        return False


def select_menu():
    print()
    print('======================================================================================')
    print(' 1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 종료')
    print('======================================================================================')
    try:
        menu = int(input('>> 메뉴 선택: '))
        return menu
    except ValueError:
        print('결과 : 숫자를 입력해주세요')
        return -1  # 잘못된 입력 시 -1 반환


def input_not_empty(prompt):
    """빈 문자열 입력 방지"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('결과 : 빈 값은 입력할 수 없습니다. 다시 입력해주세요')


mservice = MemberService()
user_no_counter = 1  # 회원번호 자동 부여

print()
print('===================== 회원 관리 =====================')

while True:
    try:
        menu = select_menu()

        if menu == 0:
            break

        elif menu == -1:
            continue  # 메뉴 입력 오류 시 다시 메뉴 출력

        # 회원가입
        elif menu == 1:
            try:
                user_id = input_not_empty('> 아이디    : ')
                if mservice.is_duplicate_id(user_id):
                    print('결과 : 이미 사용 중인 아이디입니다')
                else:
                    pw      = input_not_empty('> 비밀번호  : ')
                    name    = input_not_empty('> 이름      : ')
                    phone   = input_not_empty('> 전화번호  : ')
                    address = input_not_empty('> 주소      : ')
                    mservice.register_member(user_no_counter, user_id, pw, name, phone, address)
                    print(f'결과 : 회원가입이 완료되었습니다 (회원번호: {user_no_counter})')
                    user_no_counter += 1
            except Exception as e:
                print(f'결과 : 회원가입 중 오류가 발생했습니다 → {e}')

        # 회원목록
        elif menu == 2:
            try:
                member_list = mservice.member_list()
                if not member_list:
                    print('결과 : 등록된 회원이 없습니다')
                else:
                    for member in member_list:
                        print(member)
            except Exception as e:
                print(f'결과 : 회원목록 조회 중 오류가 발생했습니다 → {e}')

        # 회원상세정보
        elif menu == 3:
            try:
                user_id = input_not_empty('> 아이디 : ')
                member = mservice.info_member_by_id(user_id)
                if member:
                    print(member)
                else:
                    print('결과 : 해당 아이디의 회원이 없습니다')
            except Exception as e:
                print(f'결과 : 회원 조회 중 오류가 발생했습니다 → {e}')

        # 회원정보수정
        elif menu == 4:
            try:
                user_id = input_not_empty('> 아이디        : ')
                member = mservice.info_member_by_id(user_id)
                if member is None:
                    print('결과 : 존재하지 않는 회원입니다')
                else:
                    pw      = input_not_empty('> 현재 비밀번호 : ')
                    new_pw  = input_not_empty('> 새 비밀번호   : ')
                    name    = input_not_empty('> 새 이름       : ')
                    phone   = input_not_empty('> 새 전화번호   : ')
                    address = input_not_empty('> 새 주소       : ')
                    if mservice.edit_member(user_id, pw, name, new_pw, phone, address):
                        print('결과 : 회원정보가 수정되었습니다')
                    else:
                        print('결과 : 비밀번호가 일치하지 않습니다')
            except Exception as e:
                print(f'결과 : 회원정보 수정 중 오류가 발생했습니다 → {e}')

        # 회원탈퇴
        elif menu == 5:
            try:
                user_id = input_not_empty('> 아이디   : ')
                member = mservice.info_member_by_id(user_id)
                if member is None:
                    print('결과 : 존재하지 않는 회원입니다')
                else:
                    pw = input_not_empty('> 비밀번호 : ')
                    if mservice.del_member(user_id, pw):
                        print('결과 : 회원탈퇴가 완료되었습니다')
                    else:
                        print('결과 : 비밀번호가 일치하지 않습니다')
            except Exception as e:
                print(f'결과 : 회원탈퇴 중 오류가 발생했습니다 → {e}')

        else:
            print('결과 : 올바른 메뉴 번호를 입력해주세요')

    except KeyboardInterrupt:
        print('\n결과 : 프로그램을 강제 종료합니다')
        break
    except Exception as e:
        print(f'결과 : 예기치 않은 오류가 발생했습니다 → {e}')

print()
print('================== 이용해 주셔서 감사합니다 ==================')
