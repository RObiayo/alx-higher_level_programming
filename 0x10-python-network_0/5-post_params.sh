#!/bin/bash
# send a POST request to the passed URL using curl, then display the body of the outcome
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
