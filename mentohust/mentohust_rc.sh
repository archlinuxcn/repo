#!/bin/bash

. /etc/rc.conf
. /etc/rc.d/functions

#Author:    Shen Miren <dickeny@gmail.com>
#Date:		2010-01-16

NAME=mentohust
DAEMON=/usr/bin/mentohust
GATEWAY=`route -n | grep "0.0.0.0\s*UG" | awk '{print $2}'`

kill_daemon(){
    $DAEMON -k >& /dev/null
}

exec_daemon(){
    if [ -x "$DAEMON" ]; then
        $DAEMON >& /dev/null &
    fi
}

case "$1" in
	start)
		if ! ck_daemon $NAME; then
			echo "$NAME is already running.  Try '/etc/rc.d/$NAME restart'"
			exit
		fi
		stat_busy "Starting $NAME"
        exec_daemon
        # try to ping gateway
        if [ "`ping -c 4 $GATEWAY | grep ttl `" != "" ] ; then
            add_daemon $NAME
            stat_done
        else
            kill_daemon
            stat_fail
        fi
		;;
	stop)
		stat_busy "Stopping $NAME"
		kill_daemon
		rm_daemon $NAME
		stat_done
		;;
	restart)
        $0 stop
        sleep 3
        $0 start
		;;
	*)
		echo "usage: $0 {start|stop|restart}"  
esac

