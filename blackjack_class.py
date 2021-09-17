# Blackjack game python implementation.
# This file including all the classes.
import random

# Card class.
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def getSuit(self):

        return self.suit

    def getRank(self):

        return self.rank

    def getString(self):

        return self.suit + " " + self.rank + "; "

class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten',
        'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):

        self.cards = []

    # Generate a new deck of cards and shuffle it.
    def shuffle(self):

        self.cards = []

        for s in self.suits:
            for r in self.ranks:
                self.cards.append(Card(s, r))

        for i in reversed(range(1, len(self.cards))):
            j = random.randrange(i + 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # Pop one card from array.
    def dealOneCard(self):

        return self.cards.pop()

    # Get the numeric value of a given rank.
    def getCardValue(self, ranks):

        return self.values[ranks]

    # Return the number of cards that left in the array.
    def getCardsCount(self):

        return len(self.cards)

    # If the cards array is emptly, return true.
    def hasNoCard(self):

        return not self.cards

    # Print all the cards stored in the array.
    def printCards(self):

        num = 1

        for c in self.cards:
            print("{}. {}".format(num, c.getString()))
            num = num + 1

# Dealer class
class Dealer:

    def __init__(self):

        self.cards = []
        self.name = "Dealer"

    def getName(self):

        return self.name

    def showCards(self):

        card = self.cards[0]
        print("1. {}".format(card.getString()))
        print("2. **hidden**")

    def showAllCards(self):

        num = 1
        for c in self.cards:
            print("{}. {}".format(num, c.getString()))
            num = num + 1

    def addCard(self, card):

        self.cards.append(card)

    def getCards(self):

        return self.cards

    # Empty cards array.
    def reset(self):

        self.cards = []

# Player class
class Player:

    def __init__(self, name, money):

        self.name = name
        self.money = money
        self.bet = 0
        self.cards = []
        self.hit = False
        self.double_downed = False
        self.split = False

    def setName(self, name):

        self.name = name

    def getName(self):

        return self.name

    def setMoney(self, money):

        self.money = money

    def getMoney(self):

        return self.money

    def hasNoMoney(self):

        return not self.money

    def setHit(self):

        self.hit = True

    def isHit(self):

        return self.hit

    def setSplit(self):

        self.split = True

    # Check if the object is splited from the other player object.
    def isSplit(self):

        return self.split

    def setBet(self, bet):

        if bet > self.money:
            self.bet = self.money
        else:
            self.bet = bet

    def getBet(self):

        return self.bet

    def doubleBet(self):

        self.bet = self.bet * 2
        self.double_downed = True

    # Check if the player is double downed.
    def isDoubled(self):

        return self.double_downed

    def addCard(self, card):

        self.cards.append(card)

    def popCard(self):

        return self.cards.pop()

    def getCards(self):

        return self.cards
        num = num + 1

    def getCardsCount(self):

        return len(self.cards)

    def showCards(self):

        num = 1
        for c in self.cards:
            print("{}. {}".format(num, c.getString()))

    # Reset the player to the initial stat.
    def reset(self, win):

        if win:
            self.money += self.bet
        else:
            self.money -= self.bet
        self.bet = 0
        self.cards = []
        self.hit = False
        self.double_downed = False
        self.split = False

class Bot:

    dealer_upcard_to_index = { "2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "10":8, "A":9 }

    hard_totals = { "5" : ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
                    "6" : ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
                    "7" : ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
                    "8" : ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
                    "9" : ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
                    "10": ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
                    "11": ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
                    "12": ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
                    "13": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    "14": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    "15": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    "16": ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    "17": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] }

    soft_totals = { "A,2": ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
                    "A,3": ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
                    "A,4": ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
                    "A,5": ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
                    "A,6": ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
                    "A,7": ["DS", "DS", "DS", "DS", "DS", "S", "S", "H", "H", "H"],
                    "A,8": ["S", "S", "S", "S", "DS", "S", "S", "S", "S", "S"],
                    "A,9": ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] }

    pair_split = { "A,A": ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
                   "T,T": ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
                   "9,9": ["Y", "Y", "Y", "Y", "Y", "N", "Y", "Y", "N", "N"],
                   "8,8": ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
                   "7,7": ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
                   "6,6": ["Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "N"],
                   "5,5": ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
                   "4,4": ["N", "N", "N", "Y", "Y", "N", "N", "N", "N", "N"],
                   "3,3": ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
                   "2,2": ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"] }

    def __init__(self):

        return

    def isBot(self, name):

        b1 = name.find("Bot")
        b2 = name.find("bot")

        if b1 == -1 and b2 == -1:
            return False
        else:
            return True

    def bet(self, money):

        return random.randrange(money)

    def optHardHand(self, hand, dealer_upcard):

        index = self.dealer_upcard_to_index[dealer_upcard]
        opts = hard_totals[hand]
        return opts[index]

    def optSoftHand(self, hand, dealer_upcard):

        index = self.dealer_upcard_to_index[dealer_upcard]
        opts = soft_totals[hand]
        return opts[index]

    def optSplit(self, hand, dealer_upcard):

        index = self.dealer_upcard_to_index[dealer_upcard]
        opts = pair_split[hand]
        return opts[index]

class Game:

    def __init__(self):

        self.deck = Deck()
        self.dealer = Dealer()
        self.players = []
        self.players_count = 0
        self.split_count = 0
        self.turn = 0

    def newGame(self):

        self.split_count = 0
        self.turn = 0

        self.deck.shuffle()

        for p in self.players:
            p.reset()

        self.dealer.reset()

    def addPlayer(self, name, money):

        self.players.append(Player(name, money))
        self.players_count += 1

    def addSplit(self, s_player):

        n = self.players_count

        for i in range(0, n):
            p = self.players[i]
            if p.getName() == s_player.getName():
                self.players.insert(i + 1, s_player)

        self.split_count += 1

    def turn(self):

        total_count = self.players_count + self.split_count
        self.turn = self.turn % total_count
        self.turn += 1

    def getPlayer(self):

        return self.players(self.turn)

    def getPlayers(self):

        return self.players

    def isDealersTurn(self):

        if self.turn == self.players_count:
            return True

        return False

    # Dealer's turn. Dealer will hit until it reach above or equal to the 18.
    def dealersTurn(self):

        cards = self.dealer.getCards()

        values = []
        values.append(self.deck.getCardValue(cards[0].getRank()))
        values.append(self.deck.getCardValue(cards[0].getRank()))

        total = 0
        while total < 18:

            total = 0
            for v in values:
                total += v

            while total > 21:
                values[values.index(11)] -= 10
                total -= 10

            if total < 18:
                new_card = self.deck.dealOneCard()
                self.dealer.addCard(new_card)
                cards.append(new_card)

        return total

    def dealCards(self):

        for p in self.players:
            p.addCard(self.deck)
            p.addCard(self.deck)

        self.dealer.addCard(self.deck)
        self.dealer.addCard(self.deck)

    def bet(self, bet):

        player = self.players[self.turn]
        player.setBet(bet)

    def stand(self):

        return

    def hit(self):

        player = self.players[self.turn]
        player.addCard(self.deck)
        player.setHit()

    def double(self):

        player = self.players[self.turn]
        player.addCard(self.deck)
        player.doubleBet()

    def isSplittable(self):

        player = self.player[self.turn]
        cards = player.getCards()
        cardA_value = self.deck.getValue(cards[0])
        cardB_value = self.deck.getValue(cards[1])

        if not player.isHit() and not player.isSplit() and cardA_value == cardB_value:
            return True

        return False

    def split(self):

        player = self.players[self.turn]
        s_player = Player(player.getName())
        s_player.setBet(player.getBet())
        s_player.addCard(player.popCard())
        s_player.setSplit()
        self.addSplit(s_player)

    def getValues(self):

        cards = self.players[self.turn].getCards()
        values = []

        for card in cards:
            v = self.deck.getCardValue(card.getRank())
            values.append(v)

        values.sort()

    def getTotal(self):

        values = self.getValues()

        total = 0
        for value in values:
            if value == 11 and total + value > 21:
                total += 1
            else:
                total += value

        return total

    def getHand(self):

        values = self.getValues()

        hand = ""
        sign = "soft"
        if len(values) == 2 and values[0] == values[1]:
            h = str(values[0])
            hand = h + "," + h
            sign = "split"
            return (hand, sign)

        for value in values:
            if value == 11 and total + value > 21:
                total += 1
            elif value == 11 and total + value < 21:
                hand = "A,"
                sign = "hard"
            total += value

        if sign == soft:
            h = str(total)
        else:
            h = str(total - 11)
        hand = hand + h
        return (hand, sign)

    def getDealersTotal(self):

        pass

    def isBusted(self):

        total = self.getTotal()

        if total > 21:
            return True

        return False

    def isBlackJack(self):

        total = self.getTotal()

        if total == 21:
            return True

        return False

    def showAll(self):

        for p in self.players:
            print("{}: bet={}.".format(p.getName(), p.getBet()))
            p.showCards()
            print()

        print("Dealer:")
        self.dealer.showCards()
