#!/bin/sh
CXX=${CXX:-g++}
[[ $CXX =~ clang ]] && set -- "${@//-fvar-tracking-assignments/-g}"
$CXX "${@//-Wimplicit/-Wall}" -Ofast -Wall -Wextra -Wunused-result
