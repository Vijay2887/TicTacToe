from tkinter import *
import random
import os

def assign(row, column):
    global player
    global players
    global spaces
    # print(row,column)
    if button[row][column]['text'] == "":
        spaces = spaces-1
        # print(spaces)
        
        if player == players[0]:
            button[row][column]['text'] = player
            winner = get_winner()
            
            if winner is True:
                disabel_buttons()
                label.config(text=f"'{player}' wins..!")
            else:
                if spaces==0 and winner is False:
                    label.config(text="IT'S A TIE")
                else:
                    player = players[1]
                    label.config(text=f"{player}'s turn")
        elif player == players[1]:
            button[row][column]['text'] = player
            winner = get_winner()
            
            if winner is True:
                disabel_buttons()
                label.config(text=f"'{player}' wins..!")
            else:
                if spaces==0 and winner is False:
                    label.config(text="IT'S A TIE")
                else:
                    player = players[0]
                    label.config(text=f"{player}'s turn")

def get_winner():
    # checking horizontal winner
    for row in range(3):
        if button[row][0]['text'] == button[row][1]['text'] == button[row][2]['text'] == player:
            # label.config(text=f"'{player}' wins..!")
            for i in range(3):
                button[row][i].config(bg='#00ff00')
            return True
        
    #checking vertical winner
    for column in range(3):
        if button[0][column]['text'] == button[1][column]['text'] == button[2][column]['text']== player:
            # label.config(text=f"'{player}' wins..!")
            for i in range(3):
                button[i][column].config(bg='#00ff00')
            return True
        
        
    #checking diagonal winner
    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] == player:
        # label.config(text=f"'{player}' wins..!")
        for r in range(3):
            for c in range(3):
                if(r==c):
                    button[r][c].config(bg='#00ff00')
        return True  
    elif button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] == player:
        # label.config(text=f"'{player}' wins..!")
        button[0][2].config(bg='#00ff00')
        button[1][1].config(bg='#00ff00')
        button[2][0].config(bg='#00ff00')
        return True
    
    else:
        return False
    
def disabel_buttons():
    for row in range(3):
        for column in range(3):
             if button[row][column]['text'] == "":
                button[row][column].config(state=DISABLED)

def restart_btn():
    global player
    global spaces
    spaces = 9
    player = random.choice(players)
    label.config(text=f"{player}'s turn")
    for row in range(3):
        for column in range(3):
            
            button[row][column].config(text="", bg="#f0f0f0" , state="active")

    
window = Tk()
window.geometry("600x600")

players = ['x', 'o']
player = random.choice(players)
spaces = 9

title = Label(window,text="TIC-TAC-TOE", font=("small fonts", 50, "bold"), bg="black", fg="#00ff00")
title.pack(side=TOP, fill=X)

label = Label(window, text= f"{player}'s turn", font=("Algerian",30,"bold"))
label.pack()

restart = Button(window, text="restart", font=("small fonts", 30, "bold"), command=restart_btn)
restart.pack()

frame = Frame(window)
frame.pack()

button = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, width=6, height=3,command=lambda a=row,b=column : assign(a,b), font=('algerian',20,'bold'))
        button[row][column].grid(row=row, column= column)
    


window.mainloop()