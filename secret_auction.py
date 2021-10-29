from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the Secret Auction Program")

ans=True #Flag
bidders={}

while ans:
  name=input("What's your name?\n")
  bid=int(input("What's your bid?\n"))
  bidders[name]=bid #adding key,values to the bidders dictionary.
  print("Are there any more bidders?:Yes or No")
  ans=input().lower()

  if ans=="yes":
    clear() #Clear function to hide previous bids
  elif ans=="no":
    ans=False
    max_bid=0
    winner=''
    #Accessing dict key & values
    for bidder in bidders:
      bid=bidders[bidder] 
      if bid > max_bid:
        max_bid=bid
        winner=bidder 
    print("The winner of the Secret Auction is {} with the bid of ${}".format(winner,max_bid))
    #highest_bidder(price)
    print(bidders)
  else:
    print("Wrong input")


