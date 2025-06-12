import random
item_list=["Rock","Paper","Scissor"]
comp_score=0
user_score=0
while(3):
   comp_choice= random.choice(item_list)
   user_choice= input("enter your move= Rock,Paper,Scissor")
   print(f"user choice= {user_choice} , computer choice= {comp_choice}")
   if user_choice== comp_choice:
      print("both chooses same: match tie")
      comp_score=comp_score+0
      user_score=user_score+0
      print(f"computer score is {comp_score},user score is {user_score}")
   elif user_choice=="Rock":
      if comp_choice=="Paper":
        print("computer wins")
        comp_score=comp_score+1
        user_score=user_score+0
        print(f"computer score is {comp_score},user score is {user_score}")
      else:
        print("user wins")
        comp_score=comp_score+0
        user_score=user_score+1
        print(f"computer score is {comp_score},user score is {user_score}")
   elif user_choice=="Paper":
     if comp_choice=="Scissor":
        print("computer wins")
        comp_score=comp_score+1
        user_score=user_score+0
        print(f"computer score is {comp_score},user score is {user_score}")
     else:
        print("user wins")
        comp_score=comp_score+0
        user_score=user_score+1
        print(f"computer score is {comp_score},user score is {user_score}")
   elif user_choice=="Scissor":
      if comp_choice=="Paper":
        print("user wins")
        comp_score=comp_score+0
        user_score=user_score+1
        print(f"computer score is {comp_score},user score is {user_score}")
      else:
        print("computer wins")
        comp_score=comp_score+1
        user_score=user_score+0
        print(f"computer score is {comp_score},user score is {user_score}")
   if user_score== 3:
        print("user wins the game")
        break
   elif comp_score== 3:
        print("computer wins the game")
        break
   elif user_score== 3 and comp_score== 3:
        print("game is tie retry for a win")
        break


