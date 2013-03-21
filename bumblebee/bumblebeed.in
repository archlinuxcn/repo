#!/bin/bash
# Bumblebee daemon handler script. Distro-independent script to 
start/stop
# daemon. Should be runnable in any distro but won't give any feedback.

. /etc/rc.conf
. /etc/rc.d/functions

NAME=bumblebeed
CLIENT="$(which optirun)"
BIN="$(which $NAME)"
PIDFILE=/var/run/$NAME.pid

start() {
    # Start the daemon only if there is not another instance running
    stat_busy "Starting Bumblebee"
    local pid="$(cat "$PIDFILE" 2>/dev/null)"
    kill -0  $pid >/dev/null 2>&1
    case $? in
      0) ;; # already running
      *) # Can be started
        "$BIN" --daemon >/dev/null
        add_daemon $NAME
        stat_done
        return 0
        ;;
    esac
    stat_fail
    return 1
}

stop() {
    # Stop the daemon only if there is an instance running
    stat_busy "Stopping Bumblebee"
    local pid="$(cat "$PIDFILE" 2>/dev/null)"
    kill -0  $pid >/dev/null 2>&1
    case $? in
      0) # Alive and running
        local pid="$(cat "$PIDFILE" 2>/dev/null)"
        kill -TERM $pid >/dev/null
        # give it time to end gracefully...
        local retries=10
        while [ $retries -gt 0 ]; do
            retries=$(expr $retries - 1)
            kill -0 $pid >/dev/null 2>&1
            case $? in
              0) # not ready
                sleep .5
                ;;
              *) # no need for polling anymore
                break
                ;;
            esac
        done
        # ... otherwhise just terminate it.
        kill -0 $pid >/dev/null 2>&1
        case $? in
          0) # still alive > Kill
            kill -KILL $pid >/dev/null
            ;;
          *)
            ;;
        esac
        rm_daemon $NAME
        stat_done
        ;;
      *) # Not started
        stat_done
        ;;
    esac
}

restart() {
	stop 
    sleep 0.5
    start
}

case "$1" in
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        restart
    ;;
    *)
	    echo "Usage: $0 {start|stop|restart|status}"
	    exit 1
	;;
esac
