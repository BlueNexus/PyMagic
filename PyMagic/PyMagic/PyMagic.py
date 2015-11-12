import classCards
import classPlayer

player1 = classPlayer.player()
player2 = classPlayer.player()
currentPlayer = player1

AB = classCards.Monster("Giant", 3, 3, 3, "Reach")
AC = classCards.Monster("Pig", 1, 1, 1, "None")

AB.Attack(AC)