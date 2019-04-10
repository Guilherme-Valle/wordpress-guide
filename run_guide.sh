#!/bin/bash

# Stop all containers
docker kill $(docker ps -q)
# Delete all containers
docker rm $(docker ps -a -q)

# Run another process in background
../check_server.sh &

# Run container
docker-compose up

	 

