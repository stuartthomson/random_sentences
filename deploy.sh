#!/bin/sh
heroku container:push web --app octopus-tweeter && \
heroku container:release web --app octopus-tweeter
