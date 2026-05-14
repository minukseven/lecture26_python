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
    menu = int(input('>> 메뉴 선택: '))
    return menu


mservice = MemberService()
user_no_counter = 1  # 회원번호 자동 부여

print()
print('===================== 회원 관리 =====================')

while True:
    menu = select_menu()

    if menu == 0:
        break

    # 회원가입
    elif menu == 1:
        user_id = input('> 아이디    : ')
        if mservice.is_duplicate_id(user_id):
            print('결과 : 이미 사용 중인 아이디입니다')
        else:
            pw      = input('> 비밀번호  : ')
            name    = input('> 이름      : ')
            phone   = input('> 전화번호  : ')
            address = input('> 주소      : ')
            mservice.register_member(user_no_counter, user_id, pw, name, phone, address)
            print(f'결과 : 회원가입이 완료되었습니다 (회원번호: {user_no_counter})')
            user_no_counter += 1

    # 회원목록
    elif menu == 2:
        member_list = mservice.member_list()
        if not member_list:
            print('결과 : 등록된 회원이 없습니다')
        else:
            for member in member_list:
                print(member)

    # 회원상세정보
    elif menu == 3:
        user_id = input('> 아이디 : ')
        member = mservice.info_member_by_id(user_id)
        if member:
            print(member)
        else:
            print('결과 : 해당 아이디의 회원이 없습니다')

    # 회원정보수정
    elif menu == 4:
        user_id = input('> 아이디        : ')
        member = mservice.info_member_by_id(user_id)
        if member is None:
            print('결과 : 존재하지 않는 회원입니다')
        else:
            pw      = input('> 현재 비밀번호 : ')
            new_pw  = input('> 새 비밀번호   : ')
            name    = input('> 새 이름       : ')
            phone   = input('> 새 전화번호   : ')
            address = input('> 새 주소       : ')
            if mservice.edit_member(user_id, pw, name, new_pw, phone, address):
                print('결과 : 회원정보가 수정되었습니다')
            else:
                print('결과 : 비밀번호가 일치하지 않습니다')

    # 회원탈퇴
    elif menu == 5:
        user_id = input('> 아이디   : ')
        member = mservice.info_member_by_id(user_id)
        if member is None:
            print('결과 : 존재하지 않는 회원입니다')
        else:
            pw = input('> 비밀번호 : ')
            if mservice.del_member(user_id, pw):
                print('결과 : 회원탈퇴가 완료되었습니다')
            else:
                print('결과 : 비밀번호가 일치하지 않습니다')

    else:
        print('결과 : 올바른 메뉴 번호를 입력해주세요')

print()
print('================== 이용해 주셔서 감사합니다 ==================')