#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)[0][0]
