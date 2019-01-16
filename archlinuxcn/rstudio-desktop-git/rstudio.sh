#!/bin/sh
cd `dirname $1`
export LD_LIBRARY_PATH=/usr/lib/rstudio/lib
exec /usr/lib/rstudio/bin/rstudio "$@"
