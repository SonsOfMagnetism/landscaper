##############
# Game State #
##############

# This is where we store the current state of the game
game = {"tool": 0, "money": 0}

# This is a list of tools the player can use
tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Rusty Scissors", "profit": 5, "cost": 5}
]

########################
# Game Option Function #
########################

# This function allows the player to mow a lawn and make money
def mow_lawn():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about cleaning a pool and make money
    print(f"You clean a pool with your {tool['name']} and make ${tool['profit']}")
    # Update the player's money
    game["money"] += tool["profit"]
    
# This function allows the player to see their money and tool
def check_stats():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about the player's tool and money
    print(f"You currently have ${game['money']} and are using a {tool['name']}")
    

#############
# Game Loop #
#############

while(True):
    # Prompt the player to choose an option
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [Q] Quit")
    # Execute the chosen option
    if(user_choice == "1"):
        mow_lawn()
    if(user_choice == "2"):
        check_stats()
    if(user_choice == "Q"):
        break