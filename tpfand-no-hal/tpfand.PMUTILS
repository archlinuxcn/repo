#!/bin/sh

# stop tpfand during suspend
case "$1" in
  hibernate|suspend)
    systemctl stop tpfand
  ;;
  thaw|resume)
    systemctl start tpfand
  ;;
  *) exit $NA
  ;;
esac

