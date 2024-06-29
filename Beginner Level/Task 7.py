#Task 1 : Create a list of your friends' names. The list should have at least 5 names.Create a list of tuples. Each tuple should contain a friend's name and the lengthof the name.
friends = ["Purab", "Sirsaa", "Anindita", "Lucky", "Lusi"]
lengths = [(name, len(name)) for name in friends]
print("Friends' names and their lengths:", lengths)