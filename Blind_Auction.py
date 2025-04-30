participants = {}
while True:
  print("Welcome to the secret bidding program!")
  print("")
  name = input("Enter yor name: ").capitalize()
  bid = int(input("Enter the amount you want to bid: Rs."))
  participants[name] = bid
  print("")
  more = input("Are there any other bidders (Yes or No)? ").lower()
  
  if more == "yes" :
    continue
    participants[name] = bid
    
  elif more == "no":
    max_value_person = max(participants, key=participants.get) # Corrected line
    max_value = str(participants[max_value_person])
    print("")
    print(f"{max_value_person} is the highest bidder with a bid of Rs.{max_value}!")
    print("")
    print(f"Here are the bidders with their bids: {participants}")
    break
