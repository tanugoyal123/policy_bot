#!/bin/bash

# Set the image and container name
IMAGE_NAME="bot-backend"

# Pull the latest code from the master branch
echo "Pulling the latest code from the master branch..."
git pull origin master

docker build -t bot-backend .

cd ../

docker compose up -d