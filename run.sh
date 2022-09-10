#!/bin/sh
heroku run python3 main.py tweet --type web --app octopus-tweeter
echo 'Try changing this script to say "tweet" instead of local'