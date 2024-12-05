class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
print(user_1.id)

