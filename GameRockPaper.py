import random#For generate a random number, line 38 ## Ill use gun for the choises like: rock, paper... 
print('\nWelcome to the ROCK, PAPER, SCISSORS, LIZARD, SPOCK awesome game!') 
awn = raw_input('Do you wanna play? (yes or no) \n')  #Just a question haha
while awn == 'yes':#Creating a loop from here
    
    def numgun(number):#transforming number in words
                    if number == 0:
                        return "rock"
                    elif number == 1:
                        return "Spock"
                    elif number == 2:
                        return "paper"
                    elif number == 3:
                        return "lizard"
                    elif number == 4:
                        return "scissors"
                    else:
                        return "The number is out of range!"
    
    def gunnum(gun):#transforming words in number
                    if gun == "rock":
                        return 0
                    elif gun == "spock":
                        return 1
                    elif gun == "paper":
                        return 2
                    elif gun == "lizard":
                        return 3
                    elif gun == "scissors":
                        return 4
                    else:
                        return "Invalid name!"
                        #I used this because the computer can generate a random NUMBER, so I'm transforming words in numbers
    gunt = raw_input("Choose yours! ")
    gun = gunt.lower()#To make it easier, you can write SPOCK, Spock, SpOcK, does not matter. :) 
    if gun != 'rock' and 'paper' and 'scissors' and 'spock' and 'lizard' :#I did it better the last time. Creating the option Wrong Choise, if you type something that is not part of the game.
        print 'Wrong Choice'
    else:
        cgun = random.randrange(0, 4)#generate a random number 0,1,2,3 or 4
        pgun = gunnum(gun)#player
        gunc = numgun(cgun)#computer
        dif = (pgun - cgun) % 5#logic of power
        print "Computer chooses " + gunc#it shows what the computer choosed
        if( dif == 1 or dif == 2 ):#part of the logic of power of each move like, spock or rock of the game.
            print "Computer wins, and he is laughing of you"
        elif ( dif == 4 or dif == 3 ):
            print "YOU WON! YOU ARE THE BEST!!! "
        elif( dif == 0 ):
            print "You tied!"
    awn = raw_input('Do you wanna play again?\n') #asking for the loop.
else:
    print('Thank you for play.')#just beeing nice.