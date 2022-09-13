# Domonique Janai Cano Module 7

# Created list variable for possible directions
direction = ['North', 'East', 'South', 'West']
line = '~' * 100  # Variable for formatting of the game


def show_help():
    """This function returns the help menu at any point in the game when called"""
    print(
        'To move, type: Swim North, Swim East, Swim South, or Swim West\n'
        'To inspect a relic, type: Inspect \"relic name\"\n'
        'To pick up a relic & add to inventory, type: Equip \"relic name\"\n'
        'For help, type: Help\n'
        'To quit, type: Quit'
    )
    print(line)


def welcome_message():
    """This function returns the welcome message for the game beginning. It also calls the help function
    to show the help menu at the start of the game"""
    welcome = '\n\t\t\t\t\t\tWelcome to The Lost Sea Adventure Game!\n'
    print(line, welcome + line)
    print(
        'You are a mermaid living in Atlantis...\n'
        'The King of Atlantis has lost the battle '
        'against the LEVIATHAN & it has taken his\n'
        'beloved Trident, which rules all Seven Seas.\n'
        'It is your job to return the Trident to the King.\n'
        'Swim to each of the Seven Seas & find the relics needed '
        'to defeat the terrifying LEVIATHAN!\n'
        'If you do not collect ALL 6 relics, you will surely die.'
    )
    print(line)
    show_help()


def start_game():
    """This is my main game function"""
    # Player starts in Atlantis with an empty inventory
    current_location = 'Atlantis, or The Lost Sea'
    inventory = []

    # Created a nested dictionary for the map of the game along with relics within each 'sea'
    seas = {

        'Atlantis, or The Lost Sea': {
            'North': 'Mediterranean Sea',
            'East': 'The Caspian Sea',
            'South': 'The Adriatic Sea',
            'West': 'The Persian Gulf'
        },
        'Mediterranean Sea': {
            'East': 'The Arabian Sea',
            'South': 'Atlantis, or The Lost Sea',
            'relic': 'Bow'
        },
        'The Caspian Sea': {
            'North': 'The Arabian Sea',
            'South': 'The Black Sea',
            'West': 'Atlantis, or The Lost Sea',
            'relic': 'Staff'
        },
        'The Adriatic Sea': {
            'North': 'Atlantis, or The Lost Sea',
            'East': 'The Black Sea',
            'West': 'The Red Sea',
            'relic': 'Sword'
        },
        'The Persian Gulf': {
            'East': 'Atlantis, or The Lost Sea',
            'South': 'The Red Sea',
            'relic': 'Crown'
        },
        'The Red Sea': {
            'North': 'The Persian Gulf',
            'East': 'The Adriatic Sea',
            'relic': 'Flute'
        },
        'The Arabian Sea': {
            'South': 'The Caspian Sea',
            'West': 'Mediterranean Sea',
            'relic': 'Armor'
        },
        'The Black Sea': {
            'North': 'The Caspian Sea',
            'West': 'The Adriatic Sea',
            'relic': 'LEVIATHAN'
        }
    }

    # Created a dictionary for relics to give more of a detailed description for each relic
    relics = {

        'Bow': 'An ancient bow & arrow that pierces any armor or creature\'s hide',
        'Staff': 'A Staff of Starlight that stuns & blinds any enemy who looks upon it\'s wielder',
        'Sword': 'An ancient Roman sword that will send a deadly slash thru water to enemies at a distance',
        'Crown': 'Cleopatra\'s lost crown that charms anyone who looks at the one who wears it',
        'Flute': 'A flute made of bone that will lull any creature to sleep when played',
        'Armor': 'Bronze armor that will not yield, crack, or rust for all of time'
    }

    # Called the welcome function to begin the game
    welcome_message()

    # Let the player know where they are starting and with what inventory (empty)
    print('You are ready to set out. You are in {}.'.format(current_location))
    print('Inventory: {}'.format(inventory))

    def equip_relic():
        """This is a nested function that adds items to inventory and deletes them from
        the sea they are in so they do not keep showing up every time the player goes back
        to that specific sea. Returns the updated inventory list"""
        inventory.append(seas[current_location]['relic'])
        del seas[current_location]['relic']
        print('Inventory: {}'.format(inventory))

    while True:
        '''This is a continuous loop that will execute until the player types 'Quit' '''

        swim = input('What do you want to do? : \n').split()  # First asks for player input. Splits the input
        # into a list

        # Conditions for the input. First, makes sure that they type 'Swim' and a valid direction
        if swim[0] == 'Swim' and swim[1] in direction:
            command = swim[1]
            if command in seas[current_location]:
                # Checks to see if the direction is a valid way to go from the sea dictionary
                current_location = seas[current_location][command]
                # IF valid, the current location is updated to the new sea
                if current_location in seas:
                    # Makes sure the player is in a valid location
                    if current_location == 'Atlantis, or The Lost Sea':
                        # If the player is at the starting point, there is nothing to retrieve or do but move
                        # somewhere else
                        print('You are in {}. This is home. You feel rested.'.format(current_location))
                        print('Inventory: {}'.format(inventory))
                        print(line)
                    elif current_location == 'The Black Sea':
                        # If the player gets to the final sea where the LEVIATHAN is, start to check that all relics
                        # have been collected!
                        if len(inventory) == 6:
                            # This is the win condition. If all 6 relics have been collected, the player wins the game!
                            print(
                                'You see the LEVIATHAN wrapped around the Trident!\n'
                                'You begin playing a gentle melody on the Flute to lull the creature to sleep\n'
                                'As it sleeps, you try to pry the trident away...\n'
                                'The LEVIATHAN awoke!!\n'
                                'You send a swipe with your Sword, slashing at the beast\'s heart!\n'
                                'The LEVIATHAN is too fast! It sends a deadly icy blast at you!\n'
                                'The Armor shielded you. No effect!\n'
                                'Quickly, you slam the Staff, producing a blast of Starlight!'
                                'The LEVIATHAN is stunned!\n'
                                'You try the Bow next...The arrow lands in the beast\'s eye!'
                                'It turns to look at you...\n'
                                'And is charmed by the Crown!\n'
                                'The LEVIATHAN is now your pet!\n'
                                'It yields the Trident willingly! You have won THE LOST SEA!\n'
                                'Thanks for playing! :)'
                            )
                            break
                        else:
                            # This is the losing condition. If the player has less than 6 relics, they lose!
                            print(
                                'You see the LEVIATHAN wrapped around the Trident!\n'
                                'The creature quickly sends an icy blast at you!\n'
                                'You try to dodge, but are caught in the LEVIATHAN\'s icy whirlpool!\n'
                                'You are DEAD.\n'
                                'Thanks for playing! :)'
                            )
                            break
                    else:
                        # If the player is not in Atlantis or the end of the game,
                        # they are in a sea that maybe has a relic
                        print('You are in {}'.format(current_location))
                        print('Inventory: {}'.format(inventory))
                        print(line)
                        if 'relic' in seas[current_location]:
                            # This checks if a relic is in the current sea
                            print('You have found the {}!'.format(seas[current_location]['relic']))
                        else:
                            # If no relic is present, continues on
                            continue
            else:  # If the user types a valid direction, but the direction is not in that room's keys,
                # player can't move that way & must enter another input
                print('You can\'t swim that way! Try a different direction.\n')
        elif swim[0] == 'Quit':
            # If the player types quit, the game exits
            print('Thanks for playing! Goodbye')
            break
        elif swim[0] == 'Help':
            # If the player types help, the help function is called
            show_help()
        elif swim[0] == 'Equip' and swim[1] == seas[current_location]['relic']:
            # If the player types a valid Equip relic statement, the equip_relic function is called
            relic = swim[1]
            print('{} added to inventory!'.format(relic))
            equip_relic()
            print(line)
        elif swim[0] == 'Inspect' and swim[1] == seas[current_location]['relic']:
            # If the player types a valid Inspect relic statement, the corresponding
            # relic dictionary value is returned
            relic = swim[1]
            if relic in relics:
                # Checks to make sure the relic is a valid dictionary key
                print(relics[relic])
                print(line)
            else:
                # IF the relic is not valid, tells the player to try again
                print('Invalid entry. Try again:\n')
        else:
            # If no valid entry was given by the player, tells the player to try again!
            print('Invalid entry. Try again:\n')


start_game()
