#!/bin/sh
# Always run Google Earth from this shell script and not directly!
# This script makes sure the app looks in the right place for libraries
# that might also reside elsewhere.
#
# Ryan C. Gordon,  Thu Jul 20 14:32:33 PDT 2006

# We alredy know the path
cd /opt/google/earth/free

## Fix the coordinates regression:
## http://productforums.google.com/forum/#!msg/earth/dlzBfGl4eKM/723naNYBo30J
#export LC_NUMERIC=en_US.UTF-8

# Fix Panoramio along with certain crashes
LD_PRELOAD=/usr/lib/libfreeimage.so.3:./baifaao.so:/usr/lib/libpng15.so \
LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH ./googleearth-bin "$@"
