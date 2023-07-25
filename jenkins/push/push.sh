#!/bin/bash

echo "********************"
echo "** Pushing image ***"
echo "********************"

IMAGE="talyrond-backend-project"

echo "** Logging in ***"
docker login -u devopsmic -p $DOCKER_PASSWORD
echo "*** Tagging image ***"
docker tag $IMAGE:$BUILD_TAG devopsmic/$IMAGE:$BUILD_TAG
echo "*** Pushing image ***"
docker push devopsmic/$IMAGE:$BUILD_TAG
docker logout