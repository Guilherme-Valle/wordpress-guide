#!/bin/bash

# Stop all containers
docker kill $(docker ps -q)
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
#docker rmi $(docker images -q)

# Run container
docker-compose up &

# Run another process in background
../check_server.sh

docker-compose down

	 

