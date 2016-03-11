from random import randint
import urllib.request
import json

random_id = randint(1, 721)
print('Fetching Pokémon with id: {0}'.format(random_id))
request_url = 'https://pokeapi.co/api/v2/pokemon/{0}/'.format(random_id)
print('Fetching Pokémon from URL: {0}'.format(request_url))
request = urllib.request.Request(request_url, headers={"User-Agent": "Paw/2.3.1 (Macintosh; OS X/10.11.3)"})
request_body = urllib.request.urlopen(request).read().decode('utf-8')
request_body = json.loads(request_body)
print('{0}'.format(request_body['name']))

