
def admin_only(func):
    def wrapper(current_user, user, role):
        if current_user.privileges == 'Admin':
            return func(current_user, user, role)
        print(f"Действие не может быть выпонено с привилегией '{current_user.privileges}'")
        return
    return wrapper


def user_only(func):
    def wrapper(current_user, message):
        if current_user.privileges != 'ReadOnly':
            func(current_user, message)
            return
        print(f"Действие не может быть выпонено с привилегией '{current_user.privileges}'")
        return
    return wrapper


class User:
    def __init__(self, privileges: str) -> None:
        self.privileges = privileges

    @staticmethod
    @admin_only
    def change_privileges(current_user, user, role):
        user.privileges = role

    @staticmethod
    @user_only
    def post(current_user, message):
        print(message)


# user1 = User('Admin')
# user2 = User('User')
# user3 = User('ReadOnly')
#
# print(user2.privileges)
# user1.change_privileges(user3, user2, 'ReadOnly')
# print(user2.privileges)
#
# user2.post(user3, 'Hi')



