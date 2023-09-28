#!/bin/bash
# sends a JSON POST request to a URL,then displays the body of the outcome
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
