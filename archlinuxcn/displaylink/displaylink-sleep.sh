#!/bin/bash
# Copyright (c) 2015 - 2016 DisplayLink (UK) Ltd.

suspend_dlm()
{
  #flush any bytes in pipe
  while read -n 1 -t 1 SUSPEND_RESULT < /tmp/PmMessagesPort_out; do : ; done;

  #suspend DisplayLinkManager
  echo "S" > /tmp/PmMessagesPort_in

  if [ -f /tmp/PmMessagesPort_out ]; then
    #wait until suspend of DisplayLinkManager finish
    read -n 1 -t 10 SUSPEND_RESULT < /tmp/PmMessagesPort_out
  fi
}

resume_dlm()
{
  #resume DisplayLinkManager
  echo "R" > /tmp/PmMessagesPort_in
}

case "\$1/\$2" in
  pre/*)
    suspend_dlm
    ;;
  post/*)
    resume_dlm
    ;;
esac

