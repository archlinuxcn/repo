#!/bin/bash
APP=$(which $1)
ARGS=${@:2}
HASRPATH=$(chrpath -l $APP | grep -o /usr/lib)
export LIBGL_DEEPBIND=0
export LD_LIBRARY_PATH="/usr/lib/gl4es:/usr/lib/libmali/wayland:$LD_LIBRARY_PATH"
# linux linker loads the shared libs in the order of 1. RPATH of the elf, then LD_LIBRARY_PATH
# if a binary has RPATH pointed out to /usr/lib, then this causes system GL libraries to load
# in such a case we load the app directly with linker ommitting the rpath of /usr/lib
echo $HASRPATH
if [ -z $HASRPATH ]
then
    echo "Running ${APP} on Wayland with libmali"
    exec $APP $ARGS
else
    echo "Running ${APP} on Wayland with libmali using linker"
    exec /lib/ld-linux-aarch64.so.1 --inhibit-rpath :/usr/lib $APP $ARGS
fi
