#!/bin/bash

. /etc/rc.conf
. /etc/rc.d/functions
. /etc/profile.d/jdk.sh
. $DERBY_HOME/bin/derby_common.sh

DAEMON_NAME="derby-network-server"
DAEMON_CONF="/etc/conf.d/$DAEMON_NAME"
DAEMON_PID="/var/run/$DAEMON_NAME.pid"

[ -f $DAEMON_CONF ] && . $DAEMON_CONF

DERBY_START_CMD="$JAVACMD $DERBY_OPTS -classpath \"$LOCALCLASSPATH\" org.apache.derby.drda.NetworkServerControl start"
DERBY_STOP_CMD="$JAVACMD $DERBY_OPTS -classpath \"$LOCALCLASSPATH\" org.apache.derby.drda.NetworkServerControl shutdown"

case "$1" in
  start)
    stat_busy "Starting Derby Network Server"

    if ck_daemon $DAEMON_NAME; then
        $DERBY_START_CMD > /dev/null &

        PID=`ps ax | grep -v grep | grep derby | grep org.apache.derby.drda.NetworkServerControl | awk '{print $1}'`
        
        if [ -z "$PID" ]; then
            stat_fail
        else
            echo $PID > $DAEMON_PID
            add_daemon $DAEMON_NAME
            sleep 2
            stat_done
        fi    
    else
        stat_fail
    fi
    ;;
  stop)
    stat_busy "Stopping Derby Network Server"

    if ck_daemon $DAEMON_NAME; then
        stat_fail
    else
        $DERBY_STOP_CMD > /dev/null &

        if [ $? -gt 0 ]; then
            stat_fail
        else
            rm -f $DAEMON_PID
            rm_daemon $DAEMON_NAME
            stat_done
        fi
    fi
    ;;
  restart)
    $0 stop
    sleep 5
    $0 start
    ;;
  *)
    echo "usage: $0 {start|stop|restart}"
esac
exit 0

