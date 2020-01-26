"""Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file
that stries all the responses."""

filename = 'programming poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
