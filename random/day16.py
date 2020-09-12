class Database:
    def __init__(self):
        self.user = []
        self.movie = []
        self.seat = 50


class User:
    def __init__(self, user):
        self.user = user

    def addUser(self, id, name, balance):
        self.user.append([self.id, self.name, self.balance])

    def removeUser(self, id):
        for index, value in enumerate(self.user):
            if value.id == id:
                del self.user[index]

    def printUser(self, user_id=None):
        if user_id == None:
            for id, name, balance in self.user:
                print(f" {id} {name} {balance}")
        else:
            for id, name, balance in self.user:
                if id == user_id:
                    print(f" {id} {name} {balance}")


if __name__ == "__main__":
    d1 = Database()
    u1 = User(d1.user)
    print("Enter you Choice:")
    print("1. Add User")
    print("2. Remove User")
    print("3. Print All User")
    print("4. Print User Single User")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        user_id = input("Enter user id: ")
        name = input("Enter user name: ")
        balance = int(input("Enter your total balance: "))
        u1.addUser(user_id, name, balance)
    elif choice == 2:
        user_id = input("Enter the id of user you want to remove: ")
        u1.removeUser(user_id)
    elif choice == 3:
        u1.printUser()
    elif choice == 4:
        user_id = input("Enter user id to know more about the details: ")
        u1.printUser(user_id)
