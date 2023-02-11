##############
# Game State #
##############

# This is where we store the current state of the game
game = {"tool": 0, "money": 0}

# This is a list of tools the player can use
tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Rusty Scissors", "profit": 5, "cost": 5},
    {"name": "Old-Timey Push Lawnmower", "profit": 50, "cost": 25},
    {"name": "Fancy Battery Powered Lawnmower", "profit": 100, "cost": 250},
    {"name": "Team of Starving Students", "profit": 250, "cost": 500}
]

########################
# Game Option Function #
########################

# This function allows the player to mow a lawn and make money
def mow_lawn():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about mowing a lawn and making money
    print(f"You mowed a lawn with your {tool['name']} and make ${tool['profit']}")
    # Update the player's money
    game["money"] += tool["profit"]
    
# This function allows the player to see their money and tool
def check_stats():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about the player's tool and money
    print(f"You currently have ${game['money']} and are using a {tool['name']}")
    
# This function allows the player to upgrade their tool
def upgrade():
    # Check if there are no more upgrades available
    if (game["tool"]) >= len(tools) - 1:
        print("No more upgrades available")
        return 0
    # Get the next tool the player can upgrade to
    next_tool = tools[game["tool"]+1]
    # Check if the next tool is not availabe
    if (next_tool == None):
        print("There are no more tools")
        return 0
    # Check if the player has enough money to upgrade
    if (game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    # Print the message about upgrading the tool
    print("You are upgrading your tool")
    # Deduct the cost of the upgrade from the player's money
    game["money"] -= next_tool["cost"]
    # Increase the player's tool to the next level
    game["tool"] += 1

# This function checks if the player has won the game
def win_check():
    # Check if the player has upgraded the tool and has at least $1000
    if(game["money"] >= 1000):
        print("You Win")
        return True
    return False
    
#############
# Game Loop #
#############

while(True):
    # Prompt the player to choose an option
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    # Execute the chosen option
    if(user_choice == "1"):
        mow_lawn()
    if(user_choice == "2"):
        check_stats()
    if(user_choice == "3"):
        upgrade()
    if(user_choice == "4"):
        print("You quit the game")
        break
    if(win_check()):
        break