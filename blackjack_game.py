# Blackjack game python implementation.
# This file is the executable file.
import blackjack_class as bjk

banner_file_name = "blackjack_banner.txt"

bot = bjk.Bot()
game = bjk.Game()

initial_money = 2500

def showBanner():

    banner_file = open(banner_file_name, "r")
    banner_strings = banner_file.readlines()
    banner_file.close()
    for str in banner_strings:
        print(str)

def chooseGameMode():

    while True:

        print("1. Single Player.")
        print("2. Multi Player.")
        print("3. Exit.")

        valid_input_1 = ["1. Single Player.", "1", "1.", "S", "s", "Sin", "sin", "Single", "single"]
        valid_input_2 = ["2. Multi Player.", "2", "2.", "M", "m", "Mul", "mul", "Multi", "multi"]
        valid_input_3 = ["3. Exit.", "3", "3.", "E", "e", "Ex", "ex", "Exit", "exit"]

        str = input()
        if str in valid_input_1:
            return "sin"
        elif str in valid_input_2:
            return "mul"
        elif str in valid_input_3:
            return "ext"

def singlePlayer():

    print("Enter Player's Name:")

    player_name = input()
    game.addPlayer(player_name, initial_money)

def multiPlayer():

    while True:

        print("How many players? (1 ~ 10)")
        print("You can add robot by entering the name containing \"Bot\".")

        str_players = input()
        if str_players.isnumeric():
            num_players = int(str_player)
            if num_players >= 1 and num_players <= 10:
                break

    for i in range(0, num_players):

        print("Enter player{}\'s name:".format(i + 1))
        player_name = input()
        game.addPlayer(player_name, initial_money)

def betting(player):

    name = player.getName()
    money = player.getMoney()

    while True:

        print("Enter {}'s bet. (1 ~ {})".format(name, money))
        str = input()

        if str.isnumeric():
            bet = int(str)
            if bet > 0 and bet <= money:
                player.setBet(bet)
                break
# Show
def showBets():

    players = game.getPlayer()
    num = 0

    for player in players:
        num += 1
        player_name = player.getName()
        player_bet = player.getBet()
        print("{}. {} bets {}; ".format(num, player_name, player_bet))

# Game start here
showBanner()

game_mode = "nul"
while True:

    # Reset game.
    game.newGame()

    # Chose game mode
    if game_mode == "nul":

        game_mode = chooseGameMode()

        if game_mode == "sin":

            singlePlayer()

        elif game_mode == "mul":

            multiPlayer()

        elif game_mode == "ext":

            break

    # Betting
    while not isDealersTurn():

        player = game.getPlayer()


        if bot.isBot(player):
            player.setBet(bot.bet())
        else:
            betting(player)

        game.turn()

    game.showBets()
    game.turn()

    # Hitting, standing, or splitting.
    while True:
        
