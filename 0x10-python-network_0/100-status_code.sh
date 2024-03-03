#!/bin/bash
# script that sends a request to a URL passed as an argument
curl -s -o /dev/null  "$1" -w '%{http_code}'