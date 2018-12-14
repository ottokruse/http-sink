#!/bin/bash

if [[ "$CODEBUILD_BUILD_SUCCEEDING" == "0" ]]; then
    echo "Build is not succeeding!"
    exit 1
else
    echo "Build seems to be succeeding"
    exit 0
fi
