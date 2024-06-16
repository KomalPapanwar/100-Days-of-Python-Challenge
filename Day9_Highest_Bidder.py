bidder_info = {}

bidder_is_there = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

while bidder_is_there == 'yes':
    name = input("What is the name of the bidder?\n")
    value = int(input("Enter the bid value: \n$"))
    
    bidder_info[name] = value
    
    bidder_is_there = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    
highest_bid = 0
for key in bidder_info:
    if bidder_info[key] > highest_bid:
        highest_bid = bidder_info[key]
        name = key

print(f"\nThe winner is {name} with a bidding amount of ${highest_bid}") 
    