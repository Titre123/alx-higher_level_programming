#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept

curl -i "$1" | egrep 'Allow' | cut -d' ' -f 2-
