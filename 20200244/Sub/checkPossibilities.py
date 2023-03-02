def checkPossibilities(list,Username):
    "This will be the place where the entire code runs"
    marks1 = 0
    marks2 = 0
    Tied=0
    decision="yes"
    import random
    import mainMenue
    import recordTable
    #process the game
    while (decision == "yes"):
        mainMenue.myProgramme()
        player1=random.choice(list)
        player2 = input("Enter your choice here:")
        print("A:", player1)
        if (player1 == player2):
            print("Game tied. Please try again with another choice")
            Tied=Tied+1
            
        
        while (player2 == "Scissor"):
            if (player1 == "Paper"):
                print("Scissor beats Paper")
                marks2 = marks2 + 1
            elif (player1 == "Rock"):
                print("Rock beats Scissor")
                marks1 = marks1 + 1
            break
        
        while (player2 == "Paper"):
            if (player1 == "Scissor"):
                print("Scissor beats Paper")
                marks1 = marks1 + 1
            elif (player1 == "Rock"):
                print("Rock beats Paper")
                marks1 = marks1 + 1
            break
        
        while (player2 == "Rock"):
            if (player1 == "Paper"):
                print("Rock beats Paper")
                marks2 = marks2 + 1
            elif (player1 == "Scissor"):
                print("Rock beats Scissor")
                marks2 = marks2 + 1
            break
        
        decision= input("Do you want to play the game:")


    recordTable.getUserResults(str(Username),str(marks1),str(marks2),str(Tied))
    print("computer points:", marks1)
    print("user points:", marks2)
    print("Ties:",Tied)
    print("End of game")
    
   
