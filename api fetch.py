import requests
base_url = "https://pokeapi.co/api/v2/"
def something(pokemon_name):
    url = base_url+"pokemon"+"/"+pokemon_name
    req = requests.get(url)
    return req.json()
pokemon_name="squirtle"
pokemon_info = something(pokemon_name)
print(pokemon_info["height"])
print(pokemon_info["weight"])
