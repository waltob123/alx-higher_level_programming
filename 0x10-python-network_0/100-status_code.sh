#!/bin/bash
# sends a request and gets the status code curl -s -I "$1" | head -n 1 | cut -d " " -f 2
curl -s -o /dev/null -w "%{http_code}" "$1"
