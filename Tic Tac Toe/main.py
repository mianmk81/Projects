## Prolog
# Name: Dhanush Reddy Pucha and Mubashar Mian
# Email: dpucha1@student.gsu.edu, mmian1@student.gsu.edu
# Date:  11-30-22
# Section: 036

from classes import board
import replit
import random
import json
import curses


def main(scr):
    win = curses.newwin(20, 60)
    win.box()
    win.addstr(2, 2, "Hello User, You are playing")
    win.refresh()
    curses.napms(1000)
    win2 = curses.newwin(3, 50, 5, 5)
    win2.box()
    win2.addstr(1, 17, "Tic-tac-toe")
    win2.refresh()
    curses.napms(1000)
    win3 = curses.newwin(3,50 , 10, 5)
    win3.border('X', 'X', '-', '-', 'X', 'X', 'X', 'X')
    win3.addstr(1, 17, "You are the X")
    win3.refresh()
    curses.napms(1000)
    win4 = curses.newwin(3,50 , 15, 5)
    win4.addstr(1, 12, "You are joining the game")
    win4.refresh()
    curses.napms(1000)
curses.wrapper(main)

list = [1,2,3,4,5,6,7,8,9]
record = {
    
}

print(" ")
game = board()

def refresh():
    replit.clear()
    #game.display()

while True:
    game.display()
    x = int(input("\nX) enter 1 to 9: "))
    if x not in list:
        print("Please choose a different spot")
        x = int(input("\nX) enter 1 to 9: "))
        game.update_box(x, "X")
    elif x in list:
      game.update_box(x, "X")
      list.remove(x)
    refresh()
  
    if game.winner("X") == True:
        print("The player has won")
        record["Game Status"]= "You won this round"
        print(json.dumps(record))
        with open("Game_record.json", "a") as file:
          json.dump(record, file)
          file.write("\n")
          file.write("\n")
        file.close()
        play_again = input("Do you want to play again (Y/N): ")
        if play_again == "Y":
            game.reset()
            list = [1,2,3,4,5,6,7,8,9]
            continue
        else:
            break
        
    O = random.choice(list)
    if O in list:
      game.update_box(O, "O")
      list.remove(O)
    refresh()
    
    if game.winner("O") == True:
        print("The board has won")
        record["Game Status"]= "Computer Won this round"
        print(json.dumps(record))
        with open("Game_record.json", "a") as file:
          json.dump(record, file)
          file.write("\n")
          file.write("\n")
        file.close()
        play_again = input("Do you want to play again (Y/N): ")
        if play_again == "y":
          game.reset()
          list = [1,2,3,4,5,6,7,8,9]
          continue
        else:
            break

    if game.tie() == True:
        print("Tied")
        record["Game Status"]= "This round was a tie"
        print(json.dumps(record))
        with open("Game_record.json", "a") as file:
          json.dump(record, file)
          file.write("\n")
          file.write("\n")
        file.close()
        play_again = input("Do you want to play again (Y/N): ")
        if play_again == "y":
          game.reset()
          list = [1,2,3,4,5,6,7,8,9]
          continue
        else:
            break
