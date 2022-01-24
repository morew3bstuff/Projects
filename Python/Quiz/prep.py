class UserStyle1:
    pass

class UserStyle2:
    def __init__(self, id, username): # Constructor Function / Set initial values for attributes
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = UserStyle1()
user_1.id = "001"
user_1.username = "Alex"
print(user_1.__dict__) # Print all class attributes
print(user_1.id) # Print discreate attributes
print("-" * 50)

user_2 = UserStyle1()
user_2.id = "002"
user_2.username = "Mark"
print(user_2.__dict__) # Print all class attributes
print(user_2.id) # Print discreate attributes
print("-" * 50)

user_3 = UserStyle2(id="003", username="Alice") # Pass in arguments in class constructor
print(user_3.__dict__)
print(user_3.id)
print("-" * 50)

user_4 = UserStyle2(id="004", username="Sam") # Pass in arguments in class constructor
print(user_4.__dict__)
print(user_4.id)
print("-" * 50)

user_3.follow(user_4)
print(f"User 3 following: {user_3.following} people, User 4 followers: {user_4.followers}")