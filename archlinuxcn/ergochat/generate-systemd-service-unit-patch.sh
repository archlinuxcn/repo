#!/usr/bin/env bash
cd ./src/ergo/distrib/systemd/ || exit 1
LC_ALL=C TZ=UTC0 diff -Naur ergo.service{.orig,} >../../../../systemd-service-unit.patch
LC_ALL=C TZ=UTC0 diff -Naur ergo.service{.orig,} --color=always
