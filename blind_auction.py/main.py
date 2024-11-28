def record(name, amount, p_record):
    p_record['p_name'].append(name)
    p_record['p_amount'].append(amount)

def blind_auction():
    print(logo)
    times = int(input("Enter the number of participants: "))
    p_record = {'p_name': [], 'p_amount': []}
    
    for _ in range(times):
        name = input("Enter your name: ").lower()
        amount = int(input("Enter the amount you want to bid: "))
        record(name, amount, p_record)
        print("\n" * 100)  # to clear the screen
    
    max_value = max(p_record['p_amount'])  # to get the highest bid
    max_index = p_record['p_amount'].index(max_value)
    highest_bidder = p_record['p_name'][max_index]
    
    print("The highest bidder is:", highest_bidder, "with a bid of Rs.", max_value)
    print("Thanks for playing")

blind_auction()
