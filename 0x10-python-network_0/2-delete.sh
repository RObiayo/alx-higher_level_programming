#!/bin/bash
# sends a DELETE request to the URL passed as the first arg and displays the body of the outcome
curl -sX DELETE "$1"
