import requests


character_url = "http://swapi.co/api/people/"
movie_url = "http://swapi.co/api/films/"
vehicle_url = "http://swapi.co/api/vehicles/"


def get_json_response(key, url):
    response = requests.get(url)
    json_response = response.json()
    return json_response[key]


def get_info(url):
    info = requests.get(url).json()
    return info


def get_specific_info(key, url):
    urlresponse = requests.get(url).json()
    response = urlresponse.get('results')
    return response


def all_names():
    all_results = get_json_response("results", character_url)
    for character in all_results:
        print(character["name"])


def specific_names():
    user_request = input("Enter a character you would like to search for: ")
    for character in get_specific_info(user_request, character_url):
        if character.get("name").lower() == user_request.lower():
            print("Name: " + character["name"])
            print("Height: " + character["height"])
            print("Mass: " + character["mass"])
            print("Hair Color: " + character["hair_color"])
            print("Skin Color: " + character["skin_color"])
            print("Eye Color: " + character["eye_color"])
            print("Birth Year: " + character["birth_year"])
            print("Gender: " + character["gender"])
            print("Homeworld: " + character["homeworld"])
            print("")
            print("Movies the character appeared in: ")
            for movie in character["films"]:
                print(get_info(movie)["title"])
            print("")
            print("Species: ")
            for species in character["species"]:
                print(get_info(species)["name"])
            print("")
            print("Vehicles: ")
            for vehicle in character["vehicles"]:
                print(get_info(vehicle)["name"])
            print("")
            print("Starships: ")
            for starship in character["starships"]:
                print(get_info(starship)["name"])


def all_movies():
    all_results = get_json_response("results", movie_url)
    for movie in all_results:
        print(movie["title"])


def specific_movies():
    movie_request = input("Enter a movie title you would like to search for: ")
    for movie in get_specific_info(movie_request, movie_url):
        if movie.get("title").lower() == movie_request.lower():
            print("Title: " + movie["title"])
            print("Episode ID #: " + str(movie["episode_id"]))
            print("Opening Words: " + movie["opening_crawl"])
            print("Director: " + movie["director"])
            print("Producer: " + movie["producer"])
            print("Release Date: " + movie["release_date"])
            print("")
            print("Top 3 Characters: ")
            for actor in movie["characters"][:3]:
                print(get_info(actor)["name"])


def all_vehicles():
    all_results = get_json_response("results", vehicle_url)
    for vehicle in all_results:
        print(vehicle["name"])


def specific_vehicles():
    vehicle_request = input("Enter a vehicle name you would like to search for: ")
    for vehicle in get_specific_info(vehicle_request, vehicle_url):
        if vehicle.get("name").lower() == vehicle_request.lower():
            print("Vehicle Name: " + vehicle["name"])
            print("Vehicle Model: " + vehicle["model"])
            print("Manufacturer: " + vehicle["manufacturer"])
            print("Cost in Credits: " + vehicle["cost_in_credits"])
            print("Length: " + vehicle["length"])
            print("Max Speed: " + vehicle["max_atmosphering_speed"])
            print("Crew: " + vehicle["crew"])
            print("Passengers: " + vehicle["passengers"])
            print("Cargo Capacity: " + vehicle["cargo_capacity"])
            print("Consumables: " + vehicle["consumables"])
            print("Vehicle Class: " + vehicle["vehicle_class"])
            print("Pilots(if applicable): " + str(vehicle["pilots"]))
            print("")
            print("Movies the vehicle appeared in: ")
            for movie in vehicle["films"]:
                print(get_info(movie)["title"])
