import files.board
game = files.board

game.getBoardSize()

print("Selections are made in the form of row column. To make a move in the top right corner, you would enter " +
      "\'0 " + str(game.size - 1) + "\', without quotes.")
print(game.playerOneName + " will be using \'" + game.playerOneMarker + "\'; " + game.playerTwoName + " will be using \'" +
      game.playerTwoMarker + "\'\n")
game.printBoardWithLabels()
game.controlLogic()