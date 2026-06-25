from Member.member_dao import MemberDAO
from Member.member import Member

class MemberService:
    ADMIN_ID       = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, dao):
        self.__dao = dao
        self.__dao.insert_member(Member(self.ADMIN_ID, self.ADMIN_PASSWORD, '관리자'))
        self.current_user = None

    def join(self, member):
        return self.__dao.insert_member(member)

    def login(self, id, password):
        member = self.__dao.select_member_by_id(id)
        if member and member.get_password() == password:
            self.current_user = id
            return True
        return False

    def logout(self):
        self.current_user = None

    def list_members(self):
        return self.__dao.select_all_members()

    def view_member_info(self, id):
        return self.__dao.select_member_by_id(id)

    def update_member_info(self, id, member):
        return self.__dao.update_member(id, member)

    def update_member_password(self, id, org_password, new_password):
        if self.current_user != id:
            return False
        member = self.__dao.select_member_by_id(id)
        if not member or member.get_password() != org_password:
            return False
        member.set_password(new_password)
        return self.__dao.update_member(id, member)

    def remove_member(self, id):
        if self.current_user == id or self.current_user == self.ADMIN_ID:
            return self.__dao.delete_member(id)
        return False
