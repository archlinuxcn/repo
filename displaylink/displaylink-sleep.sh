#!/bin/bash
# Copyright (c) 2015 DisplayLink (UK) Ltd.

suspend_dlm()
{
  #flush any bytes in pipe
  while read -n 1 -t 1 SUSPEND_RESULT < /usr/lib/displaylink/PmMessagesPort_out; do : ; done;

  #suspend DisplayLinkManager
  echo "S" > /usr/lib/displaylink/PmMessagesPort_in

  #wait until suspend of DisplayLinkManager finish
  read -n 1 -t 10 SUSPEND_RESULT < /usr/lib/displaylink/PmMessagesPort_out
}

resume_dlm()
{
  #resume DisplayLinkManager
  echo "R" > /usr/lib/displaylink/PmMessagesPort_in
}

case "\$1/\$2" in
  pre/*)
    suspend_dlm
    ;;
  post/*)
    resume_dlm
    ;;
esac

