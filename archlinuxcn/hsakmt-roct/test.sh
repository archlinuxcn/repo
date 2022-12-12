#!/usr/bin/env sh

OUT=$(mktemp -d)
CXX=/usr/bin/g++

$CXX -I/opt/rocm/include -o "$OUT/test" test.cpp -L/opt/rocm/lib -lhsakmt
"$OUT"/test
