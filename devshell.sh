#!/bin/bash

set -e

pushd `git rev-parse --show-toplevel`

docker build -t blueair -f Dockerfile .
docker run -ti -e TZ=Europe/Amsterdam --mount type=bind,source="$(pwd)",target=/app blueair

popd
