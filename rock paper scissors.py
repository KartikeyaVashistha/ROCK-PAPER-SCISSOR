from tkinter import *
import tkinter
from PIL import ImageTk,Image
import random
root=Tk()
root.title("ROCK-PAPER-SCISSOR")
root.geometry("300x300")
root.iconbitmap("icon.ico")
#rock_photo=PhotoImage(Image.open("rock.png"))
#print(rock_photo)
option=["rock",'paper','scissor']
C_win=0
Y_win=0
def game(ch):
    global C_win
    global Y_win
    computer_choice=random.choice(option)
    choice=ch
    if ch=="rock" and computer_choice=="scissor": 
        Y_win+=1
        lb1=Label(frame,text="your choice is rock")
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW WON")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch=="rock" and computer_choice=="paper":
        C_win+=1
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW LOST")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch=="paper" and computer_choice=="rock":
        Y_win+=1
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW WON")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch=="paper" and computer_choice=="scissor":
        C_win+=1
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW LOST")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch=="scissor" and computer_choice=="rock":
        C_win+=1
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW LOST")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch=="scissor" and computer_choice=="paper":
        Y_win+=1
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="YOW WON")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
    elif ch==computer_choice:
        lb1=Label(frame,text="your choice is "+ch)
        lb1.grid(row=0,column=0)
        
        lb2=Label(frame,text="computer choice is "+computer_choice)
        lb2.grid(row=1,column=0)

        lb3=Label(frame,text="DRAW")
        lb3.grid(row=2,column=0)

        lb4=Label(frame,text="YOUR SCORE IS "+str(Y_win))
        lb4.grid(row=3,column=0)

        lb5=Label(frame,text="COMPUTER`S SCORE IS "+str(C_win))
        lb5.grid(row=4,column=0)
        


    



button_rock=Button(root,text="rock",command=lambda:game("rock"),width=25)
button_rock.grid(row=0,column=0,columnspan=1)

button_paper=Button(root,text="paper",command=lambda:game("paper"),width=25)
button_paper.grid(row=1,column=0,columnspan=1)

button_scissor=Button(root,text="scissor",command=lambda:game("scissor"),width=25)
button_scissor.grid(row=2,column=0,columnspan=1)

frame=LabelFrame(bg="orange",width=200,height=200)
frame.grid(row=4,column=0,columnspan=1)



root.mainloop()