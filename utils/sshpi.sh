#!/bin/bash

if [ "$1" = "" ]; then
    echo "usage: $0 ip"
    exit
fi

ssh -X -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@$1
