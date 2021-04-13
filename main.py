from game_data import data
from art import logo 
from art import vs
from replit import clear
import random

def formatted_data(account):
      """Takes the acct data and returns printable format"""
      account_name=account["name"]
      account_desc=account["description"]
      account_country=account["country"]
      return f"{account_name},a {account_desc} from {account_country}"

def  check_answer(guess,a_followers,b_followers):
  """Take the user guess and followers counts and returns if they got it right"""
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"
#display logo
print(logo)

score=0
game_continue=True
account_b=random.choice(data)
#Make the game repeatable
while game_continue:
  #getting random data from game_data

  #move B to A and show new data in B
  account_a=account_b
  account_b=random.choice(data)
  
  while account_a==account_b:
    account_b=random.choice(data)

  print(f"Compare A :{formatted_data(account_a)}")
  print(vs)
  print(f"Compare B : {formatted_data(account_b)}")


  #ask the user to guess
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  #check whether the user option is crt or not
  ## get followers count of each data
  a_followers_data=account_a["follower_count"]
  b_followers_data=account_b["follower_count"]

  is_correct=check_answer(guess,a_followers_data,b_followers_data)
  
  if is_correct:
    score+=1
    clear()
    print(logo)
    print(f"You are right, Current score: {score}")
  else:
    game_continue=False
    clear()
    print(logo)
    print(f"sorry, that's wrong. Final score: {score}")








