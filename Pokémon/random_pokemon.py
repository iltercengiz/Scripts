#!/usr/local/bin/python3

from random import randint
import urllib.request
import json
import os.path

def is_previous_pick(pokedex_id):
    for pokemon_data in previous_picks:
        if pokemon_data['id'] == pokedex_id:
            return True
    return False

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "previous_picks.json")
with open(path, 'r') as previous_picks_file:
    try:
        previous_picks = json.load(previous_picks_file)
    except ValueError:
        previous_picks = []

random_id = randint(1, 721)
while is_previous_pick(random_id):
    random_id = randint(1, 721)
request_url = 'https://pokeapi.co/api/v2/pokemon/{0}/'.format(random_id)
request = urllib.request.Request(request_url, headers={'User-Agent': "Paw/2.3.1 (Macintosh; OS X/10.11.3)"})
request_body = urllib.request.urlopen(request).read().decode('utf-8')
request_body = json.loads(request_body)
name = request_body['name']
print('Pokémon with id: ' + str(random_id) + ' named: ' + name)
previous_picks.append({'id': random_id, 'name': name})
with open(path, 'w') as previous_picks_file:
    json.dump(previous_picks, previous_picks_file)
    