import random

print (" --- MASTERMIND GAME --- \n")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")
print ("Initially you have 20 points\ninput sample:PRWB         //(pink,red,white,blue) \n")

colors = ["R", "G", "B", "Y", "W","P"]
attempts = 0
game = True
points=20
# computer randomly picks four-color code
color_code = random.sample(colors,4)


# player guesses the number
while game:
    correct_color = ""
    guessed_color = ""
    player_guess = input().upper()
    attempts += 1

	# checking if player's input is correct
    if len(player_guess) != len(color_code):
        print ("\nThe secret code has exactly four colors. I know, you can count to four. Try again!")
        continue
    for i in range(4):
        if player_guess[i] not in colors:
            print ("\nLook up what colors you can use in this game.\n")
            continue

	# comparison between player's input and secret code
    print(player_guess)
    if correct_color != "XXXX":
        for i in range(4):
            if player_guess[i] == color_code[i]:
                correct_color += "X"
                print ("X")

            else:
                guessed_color += "O"
                print ("0")


    if correct_color == "XXXX":
        if attempts == 1:
            print ("Wow! You guessed at the first attempt!\nYou have "+str(points)+" points\n")
            game = False
        else:
            print ("Well done... You needed " + str(attempts) + " attempts to guess.\nYou have "+str(points)+" points\n")
            game = False

    if attempts >= 1 and attempts <11 and correct_color != "XXXX":
        print ("Next attempt: ")
        points=points-2

        print ("\nYou have now "+str(points)+" points")
    elif attempts >= 11:
        print ("You didn't guess! The secret color code was: " + str(color_code)+"\nYou have "+str(points)+" points\n")
        game = False

	# play or not to play
    while game == False:
        finish_game = input("\nDo you want to play again ? if yes then Press Y . if no then press anything.").upper()
        attempts = 0
        if finish_game =="Y":
            game = True
            points=20
            print ("So, let's play again...Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)\nGuess the secret code: ")
            print ("Initially you have 20 points\ninput sample:PRWB         //(pink,red,white,blue) \n")
            color_code = random.sample(colors,4)

        else:
            print ("Thanks for the game! Bye, bye!")
            break




