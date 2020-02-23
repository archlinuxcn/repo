#!/bin/bash

readonly joplin_dir="/usr/share/joplin/"

if [[ ! -d $joplin_dir ]]; then
  echo "Cannot find /usr/share/joplin/"
  exit 1
fi

cd $joplin_dir

./joplin "$@"

