#!/bin/bash

if [ -z "$DIGITAL_OCEAN_IP_ADDRESS" ] # checking if we have a digital ocaen ip address env variable
then
    echo "DIGITAL_OCEAN_IP_ADDRESS not defined" # if the variable is not passed we will echo a message
    exit 0      # exit with status code 0
fi

# generate a tar file from git and export the latest version from our main branch
git archive --format tar --output ./project.tar main

## then we going to upload this project.tar file to the server, 
echo 'Uploading project..........Be Patient!' 
rsync ./project.tar root@$DIGITAL_OCEAN_IP_ADDRESS:/tmp/project.tar
echo 'Upload complete...'

## then we clean up our workin directory
## and decompress the source code to the working directory called app
## building our image
echo 'Building the image...'
ssh -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
    mkdir -p /app
    rm -rf /app/* && tar -xf /tmp/project.tar -C /app
    docker compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH
echo 'Build completed successfully...'
