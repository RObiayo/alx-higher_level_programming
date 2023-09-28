#!/bin/bash
# sends a request to a URL, then displays only the status code of the outcome
curl -s -o /dev/null -w "%{http_code}" "$1"
