#!/bin/bash
# This script makes a request that causes the server to respond with "You got me!"
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
