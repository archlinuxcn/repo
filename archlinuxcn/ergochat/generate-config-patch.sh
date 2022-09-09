#!/usr/bin/env bash
cd ./src/ergo/ || exit 1
LC_ALL=C TZ=UTC0 diff -Naur default.yaml{.orig,} >../../config.patch
LC_ALL=C TZ=UTC0 diff -Naur default.yaml{.orig,} --color=always
