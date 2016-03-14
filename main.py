from main import all_names, all_movies, all_vehicles, specific_names, specific_movies, specific_vehicles

while True:
    print("Welcome to the Star Wars Database Search System")
    sw_input = input("For all movies, enter 1. All people, 2. All vehicles, 3. Or for more options, enter 4. ")

    if sw_input == "1":
        all_movies()

    elif sw_input == "2":
        all_names()

    elif sw_input == "3":
        all_vehicles()

    elif sw_input == "4":
        specific_input = input("For a specific character, enter 1. Movie, enter 2. Vehicle, enter 3. ")
        if specific_input == "1":
            specific_names()
        elif specific_input == "2":
            specific_movies()
        elif specific_input == "3":
            specific_vehicles()
        else:
            print("Invalid input.")
    else:
        print("Invalid input. Must be 1, 2, or 3.")
        continue
