from Member.member import Member

class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self, member):
        if member.get_id() in self.__memberDB:
            return False
        self.__memberDB[member.get_id()] = member
        return True

    def select_member_by_id(self, id):
        return self.__memberDB.get(id, None)

    def select_all_members(self):
        return list(self.__memberDB.values()) if self.__memberDB else None

    def update_member(self, id, member):
        if id in self.__memberDB:
            self.__memberDB[id] = member
            return True
        return False

    def delete_member(self, id):
        if id in self.__memberDB:
            del self.__memberDB[id]
            return True
        return False

    def is_exist(self, id):
        return id in self.__memberDB
