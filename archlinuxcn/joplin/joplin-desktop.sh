#!/bin/bash

readonly joplin_dir="/usr/share/joplin-desktop/"

if [[ ! -d $joplin_dir ]]; then
  echo "Cannot find /usr/share/joplin-desktop/"
  exit 1
fi

cd $joplin_dir

./@joplinapp-desktop "$@"

