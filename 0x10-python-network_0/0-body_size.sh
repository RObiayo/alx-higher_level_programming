#!/bin/bash
# sends a request to a URL with curl, then displays the size of the body of the response
curl -s "$1" | wc -c
