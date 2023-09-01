#!/bin/bash
# displays all http methods the server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2
