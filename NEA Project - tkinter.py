from tkinter import *
from tkinter import ttk
import random
f=open("results.txt", "a")

def auth():

  user1="1"
  pass1="2"
  user2="3"
  pass2="4"
  user1_attempt=3
  user2_attempt=3
  user1_login = False
  user2_login = False

  while user1_login == False:
    user1_inp=str(input("Enter Player 1 username: "))
    pass1_inp=str(input("Enter Player 1 password: "))

    if user1_inp == user1 and pass1_inp == pass1:
      print("Player 1 login successful.")
      user1_login = True
    else:
      user1_attempt-=1
      print("Player 1 login unsuccessful.",user1_attempt,"Tries remaining.")
      if user1_attempt == 0:
        return False
    

  while user2_login == False:
    user2_inp=str(input("Enter Player 2 username: "))
    pass2_inp=str(input("Enter Player 2 password: "))

    if user2_inp == user2 and pass2_inp == pass2:
      print("Player 2 login successful.")
      user2_login = True
    else:
      user2_attempt-=1
      print("Player 2 login unsuccessful.",user2_attempt,"Tries remaining.")
      if user2_attempt == 0:
        return False
  return True

def diceroll():
  root=Tk()
  frm = ttk.Frame(root, padding=10)
  frm.grid()
  b1=Button(frm, text="Next turn", command=root.destroy)
  b1.place(x=300,y=0)
  b1.pack()
  dice=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
  roll1=random.randint(1,6)
  roll2=random.randint(1,6)
  total=roll1+roll2
  l1=Label(frm, text=f"{dice[roll1-1]}{dice[roll2-1]}", font=("Helvetica",260))
  l1.pack() 

  if total % 2 == 0:
    l2=Label(frm,text="Total is even. Adding 10...")
    l2.pack()
    total += 10
  else:
    l2=Label(frm,text="Total is odd. Subtracting 5...")
    l2.pack()
    total -= 5

  if roll1==roll2:
    roll3=random.randint(1,6)
    l3=Label(frm,text=f"Double! Extra roll: {roll3}")
    l3.pack()
    total += roll3

  root.mainloop()

  return total

userauth=auth()
if userauth==True:
  user1_total=0
  user2_total=0
  for x in range(0,5,1):
    print("User 1's turn")
    roll=diceroll()
    user1_total += roll
    if user1_total < 0:
      user1_total=0
    print("User 1 scored",roll,". Their total score is",user1_total)

    print("User 2's turn")
    roll=diceroll()
    user2_total += roll
    if user2_total < 0:
      user2_total=0
    print("User 2 scored",roll,". Their total score is",user2_total)

  if user1_total > user2_total:
    print("User 1 wins!")
    f.write("Winner: Tom \nScore:"+str(user1_total)+"\n")
  elif user1_total < user2_total:
    print("User 2 wins!")
    f.write("Winner: Arnold \nScore:"+str(user2_total)+"\n")
  elif user1_total == user2_total:
    print("the score is tied")
    win=False
    while win == False:
      finalroll=[random.randint(1,6),random.randint(1,6)]
      print("User 1 rolled",finalroll[0])
      print("User 2 rolled",finalroll[1])

      if finalroll[0] > finalroll[1]:
        print("User 1 wins!")
        f.write("Winner: Tom \nScore:"+str(user1_total)+"\n")
        win=True
      elif finalroll[0] < finalroll[1]:
        print("User 2 wins!")
        f.write("Winner: Arnold \nScore:"+str(user2_total)+"\n")
        win=True
      else:
        print("The tiebreaker was a tie!")

  f.close()
