def login(database, username, password):
    if((username in database) and (database[username] == password)): # same as (database.get(username) == password)
        print(f"\nWelcome back {username}!")
        return username
    elif ((username in database) and (database[username] != password)): 
        print("\nIncorrect password. Please try again.")
        return ""
    else:
         # dynamic message with username
        print(f"\n{username} not found. Please register.")
        # print("User not found. Please register.") // static message
        return ""