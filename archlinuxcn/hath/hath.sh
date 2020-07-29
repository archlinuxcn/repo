#!/bin/bash

exec /usr/bin/java -jar /usr/share/java/hath/hath.jar \
     --cache-dir=/var/lib/hath/cache \
     --data-dir=/var/lib/hath/data \
     --log-dir=/var/lib/hath/log \
     --temp-dir=/var/lib/hath/temp \
     "$@"
