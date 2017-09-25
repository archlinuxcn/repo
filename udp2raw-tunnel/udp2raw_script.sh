#!/bin/bash
CONF_FILE="$1"
TARGET="$2"
RULE=`/sbin/su -s /bin/bash nobody -c "/usr/bin/udp2raw -g --conf-file $CONF_FILE"`

if [[ "$RULE" =~ ^(.*?)iptables\ \-I\ (.*?)\ \-j\ DROP(.*?)$ ]]; then
  RULE="${BASH_REMATCH[2]}"
else
  echo "Malformed output"
  exit 1
fi

if [[ "$TARGET" == 'insert' ]]; then
  /usr/bin/iptables -I $RULE -j DROP || exit 1
elif [[ "$TARGET" == 'delete' ]]; then
  /usr/bin/iptables -D $RULE -j DROP || exit 1
fi
