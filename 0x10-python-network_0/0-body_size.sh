#!/bin/bash
# make a request to a URL using curl and returns the size of the body of the response
curl -s "$1" | wc -c
