"""
The Haunted Mansion
    Project By FadiSobhy
"""

import time
import random
import sys

Traps = ["Rock", "Stick", "Banana peel"]
trap = random.choice(Traps)  # To choice Random Options


# Restart Function To Allow Users To Play Again
def restart():
    """ This function allows players to play the game again starting from an entrance
        By a certain condition, if the player chooses Y, he can play again,
        and if he chooses n, the function exits
    """
    while True:
        restart_game = input("you want to restart the game (y/n)".title())
        if restart_game[0].lower().strip() == "y":
            print("\nlet's go to restart the game".title())
            entrance()

        elif restart_game[0].lower().strip() == "n":
            print("\nThank you for playing game, and see you soon".title())
            sys.exit()
        else:
            print_pause("\nInvalid Syntax Choose Between (y/n)")


# Function to print messages after two seconds
def print_pause(message):
    """
    print_pause function it takes the sentence used to print sentences after two seconds
    by Using import time >> time.sleep(speedtime),
    you can delay or advance the time of sentence presentation
    """
    print(message)
    time.sleep(1)


# Function To Print Final OF Story
def final():
    print_pause("\nCongratulations!!! You have Successfully")
    print_pause("Investigated The Haunted Mansion")
    print_pause("And Uncovered The Mystery Behind The Curse. You have Managed")
    print_pause("to appease the spirits and lift the curse from the mansion.")
    print_pause("You have won the game!  However, if you made the wrong choices")
    print_pause("during the game, the mansion's curse might ")
    print_pause("have taken hold of you,")
    print_pause("and you might have never returned. "
                "In that case, you have lost the game!")


# Function Chapter three basement
def basement():
    print_pause("\nChapter 3: The Basement".title())
    print_pause("You find a set of stairs leading down to the basement.".title())
    print_pause("The basement is dark, and you can barely see anything."
                "You hear strange noises coming from the darkness.Do You:".title())
    while True:
        print_pause("\n a) Investigate the noises and search the basement")
        print_pause(" b) Go back and tell the people that he can't reveal "
                    "the secret behind the palace")
        choose_13 = input("ENTER (a/b): >>> ".capitalize())

        if choose_13[0].lower().strip() == "a":
            # Investigate the noises and search the basement
            print_pause("\nWhen the grave went down, I felt cold,and fear, ")
            print_pause("and when the searchlight was turned on, "
                        "I saw frightening drawings and a group of papers.")

            print_pause("\nWhen reading the papers, I discovered the secret of "
                        "the palace, that the palace was built on burials for the dead.")
            while True:
                print_pause("\n a) Try to appease the spirits and lift the curse")
                print_pause(" b) Decide to leave the mansion and report your findings to")
                choose_14 = input("ENTER (a/b): >>> ".capitalize())

                if choose_14[0].lower().strip() == "a":
                    # Try to appease the spirits and lift the curse
                    print_pause("\nyou are a brave explorer who completed the puzzle")
                    final()
                    restart()

                elif choose_14[0].lower().strip() == "b":
                    # Decide to leave the mansion and report your findings to
                    print_pause("\nThe Story Is Over, and You Did Not Discover The Mystery"
                                " Behind This Palace, Unfortunately")

                    print_pause("you have lost. Whoever enters the palace "
                                "cannot leave it because of the curse of the palace")
                    restart()
                else:
                    print_pause("\nInvalid Syntax Choose Between (a/b)")

        elif choose_13[0].lower().strip() == "b":
            # Go back and tell the people that he can't reveal the secret behind the palace
            print_pause("\nUnfortunately, you have lost. Whoever enters the"
                        "palace cannot leave it because of the curse of the palace")
            print_pause("You don't deserve to be a brave explorer")
            restart()
        else:
            print_pause("\nInvalid Syntax Choose Between (a/b)")


# Function to print if user choose investigate noise
def investigate_noise():
    # Investigate the noises and search the other rooms
    print_pause("\nYou decide to investigate the noises "
                "and search the other rooms.".title())

    print_pause("When you entered the room, you were feeling afraid".title())
    print_pause("You found a loud TV :) . It seems that someone forgot"
                " to Turn off the TV".title())

    print_pause("\nNow You Must look for a way to go upstairs, "
                "contine down the hallway and look for a way to go upstairs")

    print_pause("\nWhen I completed the road, it turned out that there was a ")
    print_pause("large deserted library with a box and a lot of valuable")
    print_pause("books, and suddenly one of the library shelves fell DO You:")
    while True:
        print_pause("\n a) Open the box and complete the search in the library")
        print_pause(" b) Exit the library and complete the search in the Basement")
        choose_11 = input("ENTER (a/b): >>> ".capitalize())

        if choose_11[0].lower().strip() == "a":
            # Open the box and complete the search in the library
            print_pause("\nWhen I opened the box, I found a flashlight "
                        "in it that was still working.".title())

            print_pause("it seems that the Basement should be checked,"
                        "all the terrifying things happen in the Basement.")
            basement()

        elif choose_11[0].lower().strip() == "b":
            # Exit the library and complete the search in the Basement"
            print_pause("\nUpon exiting the library, you heard noises "
                        "from the Basement".title())
            while True:
                print_pause("\n a)Investigate the noises and search in Basement")
                print_pause(" b)Go out and inform the employer that "
                            "the minor secret cannot be revealed".title())
                choose_12 = input("ENTER (a/b): >>> ".capitalize())

                if choose_12[0].lower().strip() == "a":
                    # Investigate the noises and search in Basement
                    basement()

                elif choose_12[0].lower().strip() == "b":
                    # Go out and inform the employer that the minor secret cannot be revealed
                    print_pause("\nUnfortunately, You have lost. Whoever"
                                " Enters The Palace".title())

                    print_pause("cannot leave it because of the curse "
                                "of the palace".title())
                    print_pause("You Don't Deserve To Be a Brave Explorer")
                    restart()

                else:
                    print_pause("\nInvalid Syntax Choose Between (a/b)")
        else:
            print_pause("\nInvalid Syntax Choose Between (a/b)")


# Function Chapter two GroundFloor
def ground_floor():
    print_pause("\nChapter 2: The Ground Floor".title())
    print_pause("You Enter The Mansion and Find Yourself On The Ground Floor")
    print_pause("The air is thick with a sense of foreboding,"
                "and you can hear strange noises coming from "
                "the other rooms. Do you: ".title())
    while True:
        print_pause("\n a) Investigate The Noises and Search The Other Rooms")
        print_pause(" b) Proceed Cautiously and Stick to The Main Hallway")
        choose_7 = input("ENTER (a/b): >>> ".capitalize())

        if choose_7[0].lower().strip() == "a":
            # Investigate the noises and search the other rooms
            investigate_noise()

        elif choose_7[0].lower().strip() == "b":
            # Proceed cautiously and stick to the main hallway
            print_pause("\nYou decide to proceed cautiously and stick to the main"
                        " hallway".title())

            print_pause("The hallway is dimly lit, and the air is filled with a"
                        "thick mist. As you walk down the hallway, you can hear"
                        "faint whispers and footsteps coming from the other "
                        "rooms. Do you:".title())
            while True:
                print_pause("\n a) Investigate the noises and search the other rooms")
                print_pause(" b) Continue down the hallway and look for a way to go upstairs")
                choose_8 = input("ENTER (a/b): >>> ".capitalize())

                if choose_8[0].lower().strip() == "a":
                    # Investigate the noises and search the other rooms"
                    investigate_noise()

                elif choose_8[0].lower().strip() == "b":
                    # Continue down the hallway and look for a way to go upstairs
                    print_pause("\nWhen I completed the road, it turned out "
                                "that there was a ".title())

                    print_pause("large deserted library with a box and "
                                "a lot of valuable books,".title())

                    print_pause("and suddenly one of the library shelves fell DO You:")
                    while True:
                        print_pause("\n a) Open the box and complete the search in the library")
                        print_pause(" b) Exit the library and complete the search in the Basement")
                        choose_9 = input("ENTER (a/b): >>> ".capitalize())

                        if choose_9[0].lower().strip() == "a":
                            # Open the box and complete the search in the library
                            print_pause("\nWhen I opened the box, I found a "
                                        "flashlight in it that was still working.")

                            print_pause("Because it seems that the Basement should be checked,"
                                        "all the terrifying things happen in the Basement.")
                            basement()

                        elif choose_9[0].lower().strip() == "b":
                            # Exit the library and complete the search in the Basement"
                            print_pause("\nUpon exiting the library, "
                                        "you heard noises from the Basement".title())
                            while True:
                                print_pause("\n a)Investigate the noises and search in Basement")
                                print_pause(" b)Go out and inform the employer "

                                            "that the minor secret cannot be revealed")
                                choose_10 = input("ENTER (a/b): >>> ".capitalize())

                                if choose_10[0].lower().strip() == "a":
                                    basement()
                                elif choose_10[0].lower().strip() == "b":
                                    print_pause("\nUnfortunately, you have lost. "
                                                "Whoever enters the palace".title())

                                    print_pause("cannot leave it because of the "
                                                "curse of the palace".title())
                                    print_pause("You don't deserve to be a brave explorer")
                                    restart()
                                else:
                                    print_pause("\nInvalid Syntax Choose Between (a/b)")
                        else:
                            print_pause("\nInvalid Syntax Choose Between (a/b)")
                else:
                    print_pause("\nInvalid Syntax Choose Between (a/b)")
        else:
            print_pause("\nInvalid Syntax Choose Between (a/b)")


# Function To Print Introduction Of The Game
def introduction():
    print_pause("***********************")
    print_pause("The Haunted Mansion")
    print_pause("***********************")

    print_pause("You are a brave adventurer who has been hired to investigate "
                "a haunted mansion on the outskirts of town.".title())

    print_pause("The mansion is said to be cursed, "
                "and anyone who enters never returns.".title())

    print_pause("Your task is to investigate the mansion and uncover "
                "the mystery behind the curse.\n".title())


introduction()


# Function To Print Way If User Use Try To Search Another Way
def search_another_way():
    print_pause("\nWhile searching for a way to enter the palace, "
                "you find the broken window and as you enter the window".title())

    print_pause(f"falls on a {trap} "
                "and injure your ankle")
    while True:
        print_pause("\n a) Continue Your Investigation, "
                    "Ignoring The Injury")

        print_pause(" b) Retreat And Seek Medical Help")
        choose_4 = input("Enter (a/b): >>> ".capitalize())

        if choose_4[0].lower().strip() == "a":
            # Continue Your Investigation Ignoring The Injury
            ground_floor()
        elif choose_4[0].lower().strip() == "b":
            print_pause("\nNow you are out of the palace for "
                        "healthcare.".title())

            print_pause("But you have failed to solve "
                        "the secret of the mansion".title())
            restart()
        else:
            print_pause("\nInvalid Syntax Choose Between (a/b)")


def entrance():
    print_pause("\nChapter 1: The Entrance".title())

    print_pause("As you approach the mansion, you notice that the gate "
                "is locked.".title())
    print_pause("You must find a way to enter the mansion. Do you:".title())

    while True:
        print_pause("\n a) Look For a Way To Climb Over The Gate")
        print_pause(" b) Try To Find Another Entrance To The Mansion")
        choose_1 = input("ENTER (a/b): >>> ".capitalize())

        if choose_1[0].lower().strip() == "a":
            print_pause("\nYou decide to look for a way to climb over the gate.".title())

            print_pause("As you scan the perimeter, you notice a tree with "
                        "a branch hanging over the wall DO You:".title())

            while True:
                print_pause("\n a) Use The Tree Branch To Climb Over The Gate")
                print_pause(" b) Look For Another Way To Enter The Mansion")
                choose_2 = input("Enter (a/b): >>> ".capitalize())

                if choose_2[0].lower().strip() == "a":
                    print_pause("\nYou use the tree branch to climb over the "
                                "gate and enter the mansion.".title())

                    print_pause("However, as you land on the other side, you "
                                f"lose your footing and trip on a {trap} "
                                "You fall down and injure your ankle".title())

                    print_pause("You're in pain and can't walk properly. "
                                "You have to make a decision".title())

                    while True:
                        print_pause("\n a) Continue Your Investigation, "
                                    "Ignoring The Injury")

                        print_pause(" b) Retreat and Seek Medical Help")
                        choose_3 = input("Enter (a/b): >>> ".capitalize())

                        if choose_3[0].lower().strip() == "a":
                            # IF User Choose |...> Continue your investigation,ignoring the injury
                            ground_floor()

                        elif choose_3[0].lower().strip() == "b":
                            # Retreat and Seek Medical Help
                            print_pause("\nNow you are out of the palace for "
                                        "healthcare.".title())

                            print_pause("But you have failed to solve "
                                        "the secret of the mansion".title())
                            restart()

                        else:
                            print_pause("\nInvalid Syntax Choose Between (a/b)")

                elif choose_2[0].lower().strip() == "b":
                    # If User Choose |...> Look for another way to enter the mansion
                    search_another_way()

                else:
                    print_pause("\nInvalid Syntax Choose Between (a/b)")

        elif choose_1[0].lower().strip() == "b":
            # If User Choose |...> Try To Find Another Entrance To The Mansion
            search_another_way()

        else:
            print_pause("\nInvalid Syntax Choose Between (a/b)")


entrance()
