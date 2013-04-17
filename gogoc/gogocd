#!/bin/bash

# A script for launch gogoCLIENT at startup on Linux systems
# Version: 0.0.2
# Author: Ivan Gasperoni <gaspe at libero dot it>

. /etc/rc.conf
. /etc/rc.d/functions

PID=`pidof -o %PPID gogoc`
case "$1" in
   start)
     stat_busy "Starting Freenet6 Gateway client"
     [ -z "$PID" ] && gogoc -y > /dev/null 2> /dev/null
     if [ $? -gt 0 ]; then
       stat_fail
     else
       stat_done
     fi
     ;;
   stop)
     stat_busy "Stopping Freenet6 Gateway client"
     [ ! -z "$PID" ] && kill -HUP $PID > /dev/null 2> /dev/null
     if [ $? -gt 0 ]; then
       stat_fail
     else
       stat_done
     fi
     ;;
   restart)
     $0 stop
     sleep 10
     $0 start
     ;;
   *)
     echo "usage: $0 {start|stop|restart}"
esac
exit 0
