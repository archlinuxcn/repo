#!/bin/bash

if ! [ -d "$1" ]; then
  echo "Directory $1 is not exist"
  exit 255
fi

cd "$1" || exit 255

awkscript=$(cat <<'SCRIPT'
    /Entering/ {
      match($0, /contrib\/([^/']+)/, a)
      printf "    " a[1] ".tgz::"
    }
    /https:..github.com/ {
      sub(/\.git$/, "")
      printf $0 "/archive/"
    }
    /^[a-z0-9]+$/ {
      print $0 ".tar.gz"
    }
SCRIPT
)

git submodule foreach 'git config remote.origin.url; git rev-parse --short HEAD' | \
  gawk "$awkscript" | sort
