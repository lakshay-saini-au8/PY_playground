class Database:
    def __init__(self):
        self.user = []
        self.movie = []
        self.seat = 50


class User:
    def __init__(self, user):
        self.user = user
        self.booking = []

    def addUser(self, id, name, balance):
        self.user.append([id, name, balance, self.booking])

    def removeUser(self, id):
        for index, value in enumerate(self.user):
            if value[0] == id:
                del self.user[index]

    def printUser(self, user_id=None):
        if user_id == None:
            for id, name, balance, booking in self.user:
                print(f" {id} | {name} | {balance} | {booking}")
        else:
            for id, name, balance, booking in self.user:
                if id == user_id:
                    print(f" {id} | {name} | {balance} | {booking}")


class Moive:
    def __init__(self, movie):
        self.movie = movie

    def addMovie(self, movieId, movieName, movieRating, moiveCast, moiveBudget):
        self.movie.append(
            [movieId, movieName, movieRating, moiveCast, moiveBudget])

    def removeMoive(self, movie_Id):
        for index, value in enumerate(self.movie):
            if value[0] == movie_Id:
                del self.movie[index]

    def printMoive(self, moive_id=None):

        if moive_id == None:
            for movieId, movieName, movieRating, moiveCast, moiveBudget in self.movie:
                print(
                    f" {movieId} | {movieName} | {movieRating} | {moiveCast} | {moiveBudget}")
        else:
            for movieId, movieName, movieRating, moiveCast, moiveBudget in self.movie:
                if movieId == moive_id:
                    print(
                        f" {movieId} | {movieName} | {movieRating} | {moiveCast} | {moiveBudget}")


class Booking:
    def __init__(self, seat, user, moive):
        self.seat = seat
        self.user = user
        self.moive = moive

    def book(self, moive_id, user_id):
        moive_details = None
        user_details = None
        for value in self.moive:
            if value[0] == moive_id:
                moive_details = value

        for index, user in enumerate(self.user):
            if user[0] == user_id:
                self.user[index][3].append(moive_details)
                self.user[index][2] = int(
                    self.user[index][2]) - int(moive_details[4])
                print(f" {user[0]} | {user[1]} | {user[2]} | {user[3]}")


if __name__ == "__main__":
    d1 = Database()
    u1 = User(d1.user)
    m1 = Moive(d1.movie)
    b1 = Booking(d1.seat, d1.user, d1.movie)
    condi = True
    print()
    print("Enter your Choice:")
    print("1. Add User")
    print("2. Remove User")
    print("3. Print All User")
    print("4. Print User Single User")
    print("5. Add Moive")
    print("6. Remove Movie")
    print("7. Available Shows")
    print("8. Show Details With ID")
    print("9. Exit")
    print()
    while condi:
        print()
        print("To Go Main Menu Press: 0")
        choice = int(input("Enter Your Choice: "))
        print()
        if choice == 0:
            print()
            print("Enter your Choice:")
            print("1. Add User")
            print("2. Remove User")
            print("3. Print All User")
            print("4. Print User Single User")
            print("5. Add Moive")
            print("6. Remove Movie")
            print("7. Available Shows")
            print("8. Show Details With ID")
            print("9. Exit")
            print()
        elif choice == 1:
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
        elif choice == 5:
            movieId = input("Enter moive Id: ")
            movieName = input("Enter moive Name: ")
            movieRating = input("Enter moive Rating: ")
            moiveCast = input("Enter moive Cast: ")
            moiveBudget = input("Enter Show Price: ")
            m1.addMovie(movieId, movieName, movieRating,
                        moiveCast, moiveBudget)
        elif choice == 6:
            moive_id = input("Enter moive id remove: ")
            m1.removeMoive(moive_id)
        elif choice == 7:
            m1.printMoive()
            option = input(
                "Want book your ticket. If yes press y otherwise press n: ")
            if option == "y":
                moive_id = input("enter movie Id")
                user_id = input("enter user id")
                b1.book(moive_id, user_id)
        elif choice == 8:
            moive_id = input("Enter moive id print: ")
            m1.printMoive(moive_id)
        elif choice == 9:
            condi = False
