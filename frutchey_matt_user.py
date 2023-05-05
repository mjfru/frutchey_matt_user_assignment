class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    #? Have this method print all of the user's details on seperate lines
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print("~~~~~~~~~~~~~~~~")
    #? Have this method change this user's method status to True and set their gold card points to 200.
    #* Bonus: Implement the logic for testing if already a member and try to re-enroll the first user.
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} is already a member.")
        else:
            self.is_rewards_member = True
    # Have this method decrease the user's points by the amount specified
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough gold points to spend...yet!")
        else:
            self.gold_card_points = self.gold_card_points - amount

user1 = User("John", "Doe", "jdoe@aol.com", 35)
user2 = User("Jane", "Doe", "jadeyoknow@yahoo.com", 41)
user3 = User("Clarence", "Wigglesworth", "mrwiggles@gmail.com", 48)

# Have the first user spend 50 points
user1.spend_points(50)
# print(user1.gold_card_points) #* Outputs -50, Success

# Have the second user enroll
user2.enroll()
# print(user2.is_rewards_member) #* Outputs True, Success

# Have the second user spend 80 points
user2.spend_points(80)
# print(user2.gold_card_points) #* Outputs -80, Success
user1.display_info()
user2.display_info()
user3.display_info()

#* Bonus: Enrollment Logic, Success
# user1.enroll()
# print(user1.is_rewards_member)
# user1.enroll()

#* Bonus: Over-spending Logic, Success, although I do not understand why my original if amount > self.gold_cart_points:... didn't work.
# user3.spend_points(40)
# print(user3.gold_card_points)