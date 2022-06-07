from user import User

Options = ['Add Profile','Update information','Add work Experience']
class Admin(User):
    def __init__(self,first_name,last_name,phone_no):
        super().__init__(first_name,last_name,phone_no)
        self.privilege = Options
        self.piv = Privileges()
    def show_privilege(self):
        print("\nAll privileges are: ")
        for item in self.privilege:
            print(item.title())


class Privileges:
    def __init__(self):
        self.privilege = Options

    def show_privilege(self):
        print("\nAll privileges are: ")
        for item in self.privilege:
            print(item)