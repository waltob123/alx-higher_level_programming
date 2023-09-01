#!/bin/bash
# sends a GET request with a header variable to a URL
curl -s -H "X-School-User-Id: 98" "$1"
