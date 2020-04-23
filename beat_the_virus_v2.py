import time
import random


def print_sleep(text, pause):
    print(text)
    time.sleep(pause)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
            break

        else:
            print_sleep("Sorry Mayor. In this case, I'm going to need you"
                        " to pick from the choices...", 2)
    return response


def intro():
    print_sleep("Incoming email... Urgent message for the Mayor of BoomTown",
                2)
    print_sleep('.', 1)
    print_sleep('.', 1)
    print_sleep('.', 1)
    print_sleep('Turns out, YOU are the Mayor of BoomTown.', 2)


def open_email():
    options = ["yes","no"]
    emailresponse = valid_input("Do you want to open the email?"
                                " Type 'yes' or 'no'\n",
                                options)

    if emailresponse == "no":
        print_sleep("This message is marked 'urgent'. You'll probably get "
                    "fired if you don't open it", 2)
        open_email()

    elif emailresponse == "yes":
        print_sleep("The email reads:", 2)
        print_sleep("'A nasty virus has hit planet Zulu. "
                    "It has already killed 500 people in ZoomTown and is "
                    "about to hit BoomTown.\n", 2)
        print_sleep("Things you should know about this virus:\n", 2)
        print_sleep("1. It is highly contagious\n", 2)
        print_sleep("2. During the most contagious period, there are no "
                    "symptoms\n", 3)
        print_sleep("3. No existing vaccine can prevent this virus\n", 2)
        print_sleep("4. Once someone has been infected, they are immune "
                    "to the virus for 5 years\n", 3)
        print_sleep("You've got to act now to protect the people of "
                    "BoomTown'\n", 3)
        print_sleep("You are a little alarmed and immediately request a "
                    "report to see if BoomTown is already infected...", 3)
        print_sleep("'THERE ARE 5 CONFIMRED CASES OF THE VIRUS IN "
                    "BOOMTOWN.'\n", 3)
        print_sleep("You must decide what you will do next to protect the "
                    "people of BoomTown.", 3)


def option1(tasks):
    number = str(random.randint(10, 100))
    if "contain" in tasks:
        print_sleep("There is not enough space to contain all these people.\n"
                    "You've got to do something else to stop the spread of "
                    "the virus\n", 4)
        print_sleep("NEWS FLASH: " + number + " more people have been "
                    "confirmed to be infected with the virus.\n", 4)
        tasks.append("strike")
        lose(tasks)
    else:
        print_sleep("Great. You have contained the infected people.", 2)
        tasks.append("contain")
        print_sleep("NEWS FLASH: " + number + " more people have been "
                    "confirmed to be infected with the virus.\n", 4)
        print_sleep("We must do more to protect people from the virus.", 2)
        lose(tasks)

    decision(tasks)


def option2(tasks):
    number = str(random.randint(10, 100))
    print_sleep("You have enforced a law requiring everyone to stay at home",
                2)
    if "protect" in tasks:
        print_sleep("The citizens are already doing a good job staying "
                    "at home.", 2)
        print_sleep("NEWS FLASH: " + number + " more people have been "
                    "confirmed to be infected with the virus.\n", 4)
        print_sleep("More people are becomming ill. There's got to be "
                    "something else you can do.", 3)
        tasks.append("strike")
    else:
        print_sleep("Great. This is a good way to keep number of infections "
                    "down while you search for a solution.", 3)
        tasks.append("protect")
        print_sleep("NEWS FLASH: " + number + " more people have been  "
                    "confirmed to be infected with the virus.\n", 4)
    decision(tasks)


def option3(tasks):
    number = str(random.randint(10, 100))
    print_sleep("You have commissioned the development of a virus test", 2)
    if "test" in tasks:
        print_sleep("People are already being tested, which is great."
                    " But the number of infections is still increasing.", 2)
    else:
        if "protect" in tasks:
            print_sleep("Great idea. Now you slowed the spread of the virus, "
                        "testing will help trace who might be infected "
                        "and get them looked after.", 4)
            tasks.append("test")
            decision(tasks)
        else:
            print_sleep("NEWS FLASH: " + number + " more people have been "
                        "confirmed to be infected.", 3)
            print_sleep("We must first stop the spread of the virus.", 2)
            tasks.append("strike")
            lose(tasks)


def option4(tasks):
    number = str(random.randint(10, 100))
    print_sleep("You have comissioned for the development of a vaccine.", 2)
    if "protect" in tasks:
        print_sleep("You've already slowed the spread of the virus", 2)
        if "test" in tasks:
            print_sleep("And you know who is already immune and who is at "
                        "risk and needs the vaccine.", 3)
            print_sleep("Now is the perfect time to think about introducing "
                        "the vaccine", 3)
            print_sleep("Mayor of BoomTown, you have officially beat "
                        "the virus! CONGRATS YOU WIN!", 4)
            print_sleep("GAME OVER\n", 2)
            play_again()
        else:
            print_sleep("You still don't know how many people are immune "
                        "and how many people are at risk. It's not the best "
                        "time to introduce a vaccine.", 4)
            print_sleep("NEWS FLASH: " + number + " more people have been "
                        "confirmed to be infected with the virus.\n", 4)
            tasks.append("strike")
            lose(tasks)

    else:
        print_sleep("NEWS FLASH: " + number + " more people have been "
                    "confirmed to be infected.", 3)
        print_sleep("We must first stop the spread of the virus.", 2)
        tasks.append("strike")
        lose(tasks)


def decision(tasks):
    print_sleep("What do you want to do next?\n", 2)
    print_sleep("1. Contain the infected people\n", 2)
    print_sleep("2. Enforce a new law requiring everyone to stay at home\n", 2)
    print_sleep("3. Commission the development of mass virus tests\n", 2)
    print_sleep("4. Commission the development of a vaccine\n\n", 2)
    options = ["1", "2", "3", "4"]
    choice = valid_input("Make your decision: '1','2','3' or '4'\n",
                         options)

    if choice == "1":
        option1(tasks)

    elif choice == "2":
        option2(tasks)

    elif choice == "3":
        option3(tasks)

    elif choice == "4":
        option4(tasks)


def play_again():
    options = ["yes", "no"]
    again = valid_input("Would you like to play again? Type 'yes' or 'no'\n",
                        options)
    if again == "yes" :
        print_sleep("Great, let's go again.\n", 2)
        play_game()

    if again == "no" :
        print_sleep("Ok, see you next time.",2)
    return False


def lose(tasks):
    if tasks.count("strike") == 2:
        print_sleep("Too many people have died. You have been kicked "
                    "out of office. GAME OVER.\n", 3)
        play_again()
    else:
        decision(tasks)


def play_game():
    tasks = []
    intro()
    open_email()
    decision(tasks)


play_game()
