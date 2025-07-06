import random
print("Welcome to Black Jack Game 🎮 ♠️")
play_choice = input("Do you wanna play a game of Blackjack? Type 'y' or 'n':  ")
if play_choice.lower() == 'y':
        start = True
elif play_choice.lower() == 'n':
        start = False
while start:
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_cards = []
    computer_cards = []

    def add_user_cards():
        
        user_cards.append(random.choice(cards))

    def add_computer_cards():
            
            computer_cards.append(random.choice(cards))
    def sum_of_user_cards():
        user_sum = 0
        for i in range(len(user_cards)):
            user_sum += user_cards[i]
            i= i+1
        return user_sum
    def sum_of_computer_cards():
        computer_sum = 0
        for i in range(len(computer_cards)):
            computer_sum += computer_cards[i]
            i = i + 1
        return computer_sum
    add_user_cards()
    add_user_cards()
    add_computer_cards()
    add_computer_cards()
    print(f"Your cards are : {user_cards} and current score is : {sum_of_user_cards()}")
    print(f"Computer cards are : {computer_cards[0:1]}")
    if 11 in user_cards:
            n = int(input('You go ace do u wanna keep it 11 or 1 : '))
            index = user_cards.index(11)
            user_cards[index] = n
    add_card = input("Do you wanna add the cards 'y' or 'n' : ")
    if add_card.lower() == 'y':
        add_user_cards()
        if 11 in user_cards:
            n = int(input('You go ace do u wanna keep it 11 or 1 : '))
            index = user_cards.index(11)
            user_cards[index] = n  
        if sum_of_computer_cards() < 17:
            add_computer_cards()

        print(f"Your cards are : {user_cards} and  score is : {sum_of_user_cards()}")
        print(f"Computer cards are : {computer_cards[0:]} and score is : {sum_of_computer_cards()}")
        if sum_of_user_cards() <= 21 and sum_of_computer_cards() <= 21:
            if sum_of_user_cards() > sum_of_computer_cards():
                print("You Won 🎉")
            elif sum_of_computer_cards() > sum_of_user_cards():
                print("You Lost")
        elif sum_of_user_cards() > 21:
             print("Brust! You lost!")
        elif sum_of_computer_cards() > 21:
             print("Computer Burst! You Won 🎉")
        elif sum_of_user_cards() == sum_of_computer_cards():
             print("Its Draw!")
    elif add_card.lower() == 'n':
        print(f"Your cards are : {user_cards} and  score is : {sum_of_user_cards()}")
        print(f"Computer cards are : {computer_cards[0:2]} and score is : {sum_of_computer_cards()}")
        if sum_of_user_cards() <= 21 and sum_of_computer_cards() <= 21:
            if sum_of_user_cards() > sum_of_computer_cards():
                print("You Won 🎉")
            elif sum_of_computer_cards() > sum_of_user_cards():
                print("You Lost")
        elif sum_of_computer_cards() > 21:
             print("Computer Burst! You Won 🎉")
        elif sum_of_user_cards() == sum_of_computer_cards():
             print("Its Draw!")
        else:
             print("Brust! You Lost")
        choice = input("Do you wanna play again 'y' or 'n' : ")
        if choice.lower() == 'y':
             start = True
        elif choice.lower() == 'n':
             start = False
             print("Bye Bye!")
