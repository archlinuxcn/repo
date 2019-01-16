#!/bin/sh
source /etc/n2n/edge/$1.conf
PARAMS="-d $TUN"
[[ "z$DHCP" = "z1" ]] && PARAMS="$PARAMS -a dhcp:0.0.0.0" || PARAMS="$PARAMS -a static:$ADDRESS"
PARAMS="$PARAMS -c $COMMUNITY"
PARAMS="$PARAMS -k $KEY"
[[ -z "$NETMASK" ]] || PARAMS="$PARAMS -s $NETMASK"
[[ -z "$MACADDR" ]] || PARAMS="$PARAMS -m $MACADDR"
PARAMS="$PARAMS -l $SUPERNODE"
[[ "z$FORWADING" = "z1" ]] && PARAMS="$PARAMS -r"
[[ -z "$LPORT" ]] || PARAMS="$PARAMS -p $LPORT"
[[ -z "$MTU" ]] || PARAMS="$PARAMS -M $MTU"
[[ -z "$TPORT" ]] || PARAMS="$PARAMS -t $TPORT"
[[ "z$PRESOLV" = "z1" ]] && PARAMS="$PARAMS -b"
exec /usr/bin/edge $PARAMS -f