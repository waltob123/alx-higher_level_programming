#!/bin/bash
# a script that sends a JSON POST request to a URL
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
