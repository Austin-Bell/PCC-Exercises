#Make a list inviting three people to dinner. Use your list to print a personal message, invitng them to dinner
guest_list = ["Richard Feynman","Bill Nye","Steve Jobs"]

# add more guests to the dinner using insert() and append()
guest_list.insert(0, "Steve Wozniak")
guest_list.insert(2, "Bill Gates")
guest_list.append("Marie Curie")

messages_1 = guest_list[0] + ", You are personally invited to dinner!"
messages_2 = guest_list[1] + ", You are personally invited to dinner!"
messages_3 = guest_list[2] + ", You are personally invited to dinner!"
messages_4 = guest_list[3] + ", You are personally invited to dinner!"
messages_5 = guest_list[4] + ", You are personally invited to dinner!"
messages_6 = guest_list[5] + ", You are personally invited to dinner!"



print(guest_list)

print(messages_1)
print(messages_2)
print(messages_3)
print(messages_4)
print(messages_5)
print(messages_6)