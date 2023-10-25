# def  initialize deck.
import random


def initialize_deck():
    deck = {
        "Βαλες-κουπα": 10,
        "Βαλες-σπαθι": 10,
        "Βαλες-καρο": 10,
        "Βαλες-μπαστουνι": 10,
        "Νταμα-κουπα": 10,
        "Νταμα-σπαθι": 10,
        "Νταμα-καρο": 10,
        "Νταμα-μπαστουνι": 10,
        "Ριγας-κουπα": 10,
        "Ριγας-σπαθι": 10,
        "Ριγας-καρο": 10,
        "Ριγας-μπαστουνι": 10,
        "Ασσος-κουπα": 1,
        "Ασσος-σπαθι": 1,
        "Ασσος-καρο": 1,
        "Ασσος-μπαστουνι": 1,
        "δυο-κουπα": 2,
        "δυο-μπαστουνι": 2,
        "δυο-καρο": 2,
        "δυο-σπαθι": 2,
        "τρια-κουπα": 3,
        "τρια-σπαθι": 3,
        "τρια-καρο": 3,
        "τρια-μπαστουνι": 3,
        "τεσσερα-κουπα": 4,
        "τεσσερα-καρο": 4,
        "τεσσερα-μπαστουνι": 4,
        "τεσσερα-σπαθι": 4,
        "πεντε-κουπα": 5,
        "πεντε-σπαθι": 5,
        "πεντε-καρο": 5,
        "πεντε-μπαστουνι": 5,
        "εξι-κουπα": 6,
        "εξι-καρο": 6,
        "εξι-μπαστουνι": 6,
        "εξι-σπαθι": 6,
        "επτα-κουπα": 7,
        "επτα-καρο": 7,
        "επτα-σπαθι": 7,
        "επτα-μπαστουνι": 7,
        "οκτω-κουπα": 8,
        "οκτω-καρο": 8,
        "οκτω-μπαστουνι": 8,
        "οκτω-σπαθι": 8,
        "εννεα-κουπα": 9,
        "εννεα-καρο": 9,
        "εννεα-μπαστουνι": 9,
        "εννεα-σπαθι": 9,
        "δεκα-κουπα": 10,
        "δεκα-καρο": 10,
        "δεκα-μπαστουνι": 10,
        "δεκα-σπαθι": 10,
    }
    shuffled_cards = list(deck.keys())
    random.shuffle(shuffled_cards)
    shuffled_deck = {card: deck[card] for card in shuffled_cards}
    random_list = list(shuffled_deck.items())
    return random_list


# def for player turn.
def player_turn(deck):
    playerDeck = []
    card = random.choice(deck)
    playerDeck.append(card)
    deck.remove(card)
    newCard = random.choice(deck)
    playerDeck.append(newCard)
    deck.remove(newCard)
    while True:
        playerCardValues = 0
        count = 0
        print("----------------------------------------------------")
        print(f"Your hand is {playerDeck}")
        for card in playerDeck:
            if card[0] == 'Ασσος':
                count += 1
                if count == 2:
                    print("You won! ")
                    exit("Congrats!")
            if "Ασσος" in card[0]:
                aceChoice = int(input("Do you want to count as 1 or 11?"))
                if aceChoice == 1:
                    playerCardValues += 1
                else:
                    playerCardValues += 11 - 1
            playerCardValues += card[1]
        print(f"Your card value is: {playerCardValues}")
        if playerCardValues > 21:
            print("You Lost! Pc Won.")
            exit("Sorry you lost Player!")
        else:
            if playerCardValues == 21:
                print("You Won! ")
                exit("Congrats!")
        playerChoice = input("Do you want another card? Yes or No ")
        while playerChoice != "Yes" and playerChoice != "No":
            print("Invalid choice.Please only yes or no! ")
            playerChoice = input("Do you want another card? Yes or No ")
        if playerChoice == "No":
            break
        elif playerChoice == "Yes":
            new_card = random.choice(deck)
            playerDeck.append(new_card)
            playerDeck.remove(new_card)
        else:
            print("Invalid Choice! ")

    playerFinal = playerCardValues
    return playerFinal


# def for pc turn
def pc_turn(deck, playerCardValues):
    pcDeck = []
    pc_card = random.choice(deck)
    pcDeck.append(pc_card)
    deck.remove(pc_card)
    pc_newCard = random.choice(deck)
    pcDeck.append(pc_newCard)
    deck.remove(pc_newCard)
    while True:
        pcCount = 0
        # pc turn
        print(pcDeck)
        pcCardValues = 0
        for pcCard in pcDeck:
            if pcCard[0] == 'Ασσος':
                pcCount += 1
                if pcCount == 2:
                    print("You won! ")
                    exit("Sorry player, You Lost!")
            if "Ασσος" in pcCard[0]:
                randomPcAce = random.randint(0, 1)
                if randomPcAce == 0:
                    pcCardValues += 1
                else:
                    pcCardValues += 11 - 1
            pcCardValues += pcCard[1]
        print(f"Your card value is: {pcCardValues}")
        if pcCardValues > 21:
            print("You Lost! ")
            exit("Player Won! ")
        else:
            if pcCardValues == 21:
                print("You won!  ")
                exit("Sorry you lost Player!")
        if pcCardValues < playerCardValues:
            pcNewCard = random.choice(deck)
            pcDeck.append(pcNewCard)
            deck.remove(pcNewCard)
        else:
            pcRandomNextCard = random.randint(0, 1)
            if pcRandomNextCard == 0:
                break
            else:
                pcNewCard = random.choice(deck)
                pcDeck.append(pcNewCard)

    pcFinal = pcCardValues
    return pcFinal


# def blackJack game.
def blackJack_game():
    deck = initialize_deck()
    print("Welcome to BlackJack!\nThe rules are simple.If you have better hand than "
          "pc you will win ,otherwise you will lost!\n"
          "Warning, if passed 21 you will automatically loose!\n"
          "If there is deuce, the pc wins!")
    player_final = player_turn(deck)
    pc_final = pc_turn(deck, player_final)
    if pc_final == player_final:
        print("It's a tie! PC wins.")
    elif pc_final < player_final:
        print("Player wins!")
    else:
        print("PC wins. Sorry, you lost, Player!")
