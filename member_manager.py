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

    def member_update(self, name, phone, address):  
        self.__name = name
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

    # ✅ 회원번호 중복 확인
    def is_duplicate_no(self, user_no):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                return True
        return False

    # ✅ 아이디 중복 확인
    def is_duplicate_id(self, user_id):
        for member in self.__member_list:
            if member.get_id() == user_id:
                return True
        return False

    def register_member(self, user_no, user_id, pw, name, phone, address):
        member = Member(user_no, user_id, pw, name, phone, address)
        self.__member_list.append(member)
        return True

    def member_list(self):
        return self.__member_list

    def info_member(self, user_no):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                return member
        return None

    def edit_member(self, user_no, pw, name, phone, address):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                if member.get_pw() != pw:
                    return False
                member.member_update(name, phone, address)  # ✅ pw 제거
                return True
        return False

    def del_member(self, user_no, pw):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                if member.get_pw() != pw:
                    return False
                self.__member_list.remove(member)
                return True
        return False


Menus = [0, 1, 2, 3, 4, 5]

def select_menu():
    print('======================================================================================')
    print(' 1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 종료')
    print('======================================================================================')
    while True:
        try:
            menu = int(input('>> 메뉴 선택 :'))
            if menu in Menus:
                return menu
            print('메뉴에 있는 숫자만 입력해주세요.')
        except ValueError:
            print('메뉴에 있는 숫자만 입력해주세요.')

def input_user_no(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('숫자만 입력해주세요.')

def input_name(msg):
    while True:
        name = input(msg)
        if name.isalpha():
            return name
        print('이름은 문자만 입력해주세요.')

def input_phone(msg):
    while True:
        phone = input(msg)
        if phone.isdigit():
            return phone
        print('전화번호는 숫자만 입력해주세요.')


mservice = MemberService()

print()
print('===================== 회원관리 =====================')

while True:
    print()
    menu = select_menu()
    if menu == 0:
        break

    elif menu == 1:
        user_no = input_user_no('> 회원번호 : ')
        # ✅ 회원번호 중복 확인
        if mservice.is_duplicate_no(user_no):
            print('결과 : 이미 사용 중인 회원번호입니다.')
        else:
            user_id = input('> 아이디 : ')
            # ✅ 아이디 중복 확인
            if mservice.is_duplicate_id(user_id):
                print('결과 : 이미 사용 중인 아이디입니다.')
            else:
                pw = input('> 비밀번호 : ')
                name = input_name('> 이름 : ')
                phone = input_phone('> 전화번호 : ')
                address = input('> 주소 : ')
                mservice.register_member(user_no, user_id, pw, name, phone, address)
                print('결과 : 회원가입이 완료되었습니다.')

    elif menu == 2:
        member_list = mservice.member_list()
        if not member_list:
            print('결과 : 등록된 회원이 없습니다.')
        else:
            for member in member_list:
                print(f'회원번호: {member.get_user_no()} | 이름: {member.get_name()}')

    elif menu == 3:
        user_no = input_user_no('> 회원번호 : ')
        member = mservice.info_member(user_no)
        if member:
            print(member)
        else:
            print('결과 : 회원번호에 해당하는 회원이 없습니다.')

    elif menu == 4:
        user_no = input_user_no('> 회원번호 : ')
        member = mservice.info_member(user_no)
        if member is None:
            print('결과 : 존재하지 않는 회원입니다.')
        else:
            pw = input('> 현재 비밀번호 : ')
            if member.get_pw() != pw:
                print('결과 : 비밀번호가 일치하지 않습니다.')
            else:
                name = input_name('> 새 이름 : ')
                phone = input_phone('> 새 전화번호 : ')
                address = input('> 새 주소 : ')
                mservice.edit_member(user_no, pw, name, phone, address)
                print('결과 : 회원정보가 수정되었습니다.')

    elif menu == 5:
        user_no = input_user_no('> 회원번호 : ')
        member = mservice.info_member(user_no)
        if member is None:
            print('결과 : 존재하지 않는 회원입니다.')
        else:
            pw = input('> 비밀번호 : ')
            if mservice.del_member(user_no, pw):
                print('결과 : 회원탈퇴가 완료되었습니다.')
            else:
                print('결과 : 비밀번호가 일치하지 않습니다.')

print()
print('================== 이용해 주셔서 감사합니다 ==================')
