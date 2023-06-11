#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Gives the len of a string and its initial char."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
