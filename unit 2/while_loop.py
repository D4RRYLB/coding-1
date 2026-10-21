# Loop - a loop is a construct (special function) that repeats itself
# In programming, a loop allows to repeats code instructions

# There are two types of loops: for loop and while loop

# while loop - a type of loop where so long as a condition is equal
# to true it will keep running forever

# the keyword is while - -> do while

# syntax
num = 4
while 2+2 == num: # condition - -> operations - must be true
    print(num == 4)
    print("the program is running... ")
    num = int(input("please type in a new number: "))

# while loops will ALWAYS run unless you change the condition!
# we can do this by writing instructions to manually change it    


def guessingGame():
    correctAnswer= 10
    userguess= int(input("please type in a number to guess: "))
    attempts= 0

    while userguess != correctAnswer:
        print("sorry thats incorrect ")
        print ("try again...")
        attempts +=1
        print("number of attempts:" + str(attempts))
        userguess= int(input("please type in a number to guess:"))

    print ("congratulations you guessed correctly!")    
    print("do you want to guess again")

def passwordreset():
    password = 4985
    attempts = 4

    print("please log in using your password")
    userPwattempt = input()

    while userPwattempt != correctPw:
        print("sorry incorrect")