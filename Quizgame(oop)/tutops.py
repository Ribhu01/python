class User:

    # how to create constructor ( def __init__(self):)
    def __init__(self, user_id, username):
        print("new user is being created...")
        self.id = user_id
        self.username =  username
        self.followers =0
        self.following = 0


    def follow(self, user):
        user.followers +=1
        self.following+=1

user1 = User("001", "ribhu")
user2 = User("002", "rahul")
# how to create a attribute for user class

print(user1.id)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)