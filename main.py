import requests


def get_json_response(key, url):
    response = requests.get(url)
    json_response = response.json()
    return json_response[key]


def all_names():
    url = "http://swapi.co/api/people/"
    all_results = get_json_response("results", url)
    for person in all_results:
        print(person["name"])


def specific_names():
    url = "http://swapi.co/api/people/"
    all_results = get_json_response("results", url)
    for person in all_results:
        number = (person["url"][26:])
        new_url = "http://swapi.co/api/people" + number
        for person in get_json_response("films", new_url):
            print(get_json_response("title", person))
specific_names()


def all_movies():
    url = "http://swapi.co/api/films/"
    all_results = get_json_response("results", url)
    for person in all_results:
        print(person["title"])


def all_vehicles():
    url = "http://swapi.co/api/vehicles/"
    all_results = get_json_response("results", url)
    for person in all_results:
        print(person["name"])
