#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    """
    main: entry.
    """
    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode(
        {'email': email}).encode('utf-8')

    request = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
