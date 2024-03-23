#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    items = a_dictionary.items()
    return sorted(items, key=lambda item: item[1], reverse=True)[0][0]
