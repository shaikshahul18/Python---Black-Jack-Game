import random
def deal():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_number = random.randint(0,len(cards)-1)
    return cards[card_number]

def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "TIE"):
    if win_or_lose == 'WIN':
        print(f"Your cards are {my_cards}")
        print(f"The computer's cards are {comp_cards}")
        #print(f"The total of user is {total_user} and total of comp is {total_comp}")
        print("YOU WIN!")
    elif win_or_lose == 'LOST':
        print(f"Your cards are {my_cards}")
        print(f"The computer's cards are {comp_cards}")
        #print(f"The total of user is {total_user} and total of comp is {total_comp}")
        print("YOU LOST!")
    else:
        print(f"Your cards are {my_cards}")
        print(f"The computer's cards are {comp_cards}")
        #print(f"The total of user is {total_user} and total of comp is {total_comp}")
        print("IT'S A TIE!")

def compare(my_cards, comp_cards):
    total_user = sum(my_cards)
    total_comp = sum(comp_cards)
    if total_comp == total_user:
        #print("HERE")
        output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "TIE")
    elif total_user > 21 and total_comp > 21:
        output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "LOSE")
    elif total_user > 21 and total_comp < 21:
        output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "LOSE")
    elif total_comp > 21 and total_user < 21:
        output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "WIN")
    else:
        if total_user == 21:
            output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "WIN")
        elif total_comp == 21:
            output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "LOSE")
        else:
            if total_user < total_comp:
                output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "LOSE")
            else:
                output(my_cards,comp_cards,total_user, total_comp,win_or_lose = "WIN")

def play_game():
    play = input("Please press 'Y' if you want to play black jack or 'N':\n")
    my_cards,comp_cards = [] , []
    first_deal = True
    game = True
    while(game):
        if play == 'Y' and first_deal == True:
            first_deal = False
            for i in range(2):
                my_cards.append(deal())
                comp_cards.append(deal())
            print(f"Your cards: {my_cards}, current_score: {calculate_score(my_cards)}")
            print(f"Computer's first card: {comp_cards[0]}")
        next = input("Press 'Y' to HIT or 'N' to PASS:\n")
        if next == 'Y':
            my_cards.append(deal())
            print(f"Your cards: {my_cards}, current_score: {calculate_score(my_cards)}")
            print(f"Computer's first card: {comp_cards[0]}")
        elif next == 'N':
            #print("HERE")
            while(sum(comp_cards)<17):
                #print("HERE AGAIN")
                comp_cards.append(deal())
            compare(my_cards,comp_cards)
            game = False

play_game()
