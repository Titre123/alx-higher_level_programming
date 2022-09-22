#!/bin/bash
#  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

status = curl -i -X GET "$1" | grep 'HTTP/1.*' | awk '{print $2}'
if [ "$status" -eq 200] ; then
	curl -X GET "$1
else
	echo ""
fi
