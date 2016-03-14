from main import all_names, all_movies, all_vehicles

while True:
    print("Welcome to the Star Wars Database Search System")
    sw_input = input("To search all movies, enter 1. All people, enter 2. All vehicles, enter 3. ")

    if sw_input == "1":
        all_movies()

    elif sw_input == "2":
        all_names()

    elif sw_input == "3":
        all_vehicles()

    else:
        print("Invalid input. Must be 1, 2, or 3.")
        continue
