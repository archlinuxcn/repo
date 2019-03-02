#!/bin/sh
exec /usr/bin/java -jar /usr/share/java/hath/hath.jar --data-dir=/var/lib/hath/data --cache-dir=/var/lib/hath/cache --temp-dir=/var/lib/hath/temp --log-dir=/var/lib/hath/log "$@"