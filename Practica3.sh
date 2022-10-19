#!/bin/bash

echo 'Se usara la api de Starwars para revisar planetas, personajes etc.'
echo''
echo''
curl -s "https://swapi.dev/api/people/10"
echo''
echo''
curl -s "https://swapi.dev/api/people/8"
echo''
echo''
curl -s "https://swapi.dev/api/starships/2"
echo''
echo''
curl -s "https://swapi.dev/api/starships/1"
echo''
echo''
curl -s "https://swapi.dev/api/planets/10"
