#!/bin/sh

run_hook ()
{
  INITTY=/dev/tty[1-6]
  for tty in $INITTY; do
    /usr/bin/setleds -D +num < $tty
  done
}
