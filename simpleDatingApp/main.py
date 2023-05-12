import random


class User:
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests


class DatingApp:
    def __init__(self):
        self.users = []

    def register_user(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        interests = input("Enter your interests: ")
        new_user = User(name, age, gender, interests)
        self.users.append(new_user)
        print("User registered successfully!")

    def show_matches(self, gender, interests):
        matches = []
        for user in self.users:
            if user.gender != gender and user.interests == interests:
                matches.append(user)
        if len(matches) == 0:
            print("Sorry, no matches found.")
        else:
            print("Found", len(matches), "matches:")
            for user in matches:
                print("Name:", user.name)
                print("Age:", user.age)
                print("Gender:", user.gender)
                print("Interests:", user.interests)
                print("")

    def auto_populate_users(self):
        names = ["Bob", "Alice", "Charlie", "Emily", "Dave"]
        interests = ["sports", "music", "movies", "books"]
        for i in range(5):
            name = names[i]
            age = random.randint(18, 40)
            gender = "male" if i % 2 == 0 else "female"
            interest = random.choice(interests)
            new_user = User(name, age, gender, interest)
            self.users.append(new_user)


app = DatingApp()
app.auto_populate_users()

while True:
    print("1. Register user")
    print("2. Find matches")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        app.register_user()
    elif choice == "2":
        gender = input("Enter your gender: ")
        interests = input("Enter your interests: ")
        app.show_matches(gender, interests)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
