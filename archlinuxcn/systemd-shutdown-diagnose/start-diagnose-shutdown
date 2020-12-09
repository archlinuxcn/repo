#!/bin/bash
set -e
PS4="> ${0##*/}: "
set -x

cd /sys/kernel/debug/tracing
echo 0 >tracing_on
echo >trace

echo syscalls:sys_enter_exit >set_event
echo syscalls:sys_enter_kill >>set_event
echo syscalls:sys_enter_tkill >>set_event
echo syscalls:sys_enter_tgkill >>set_event
echo signal:signal_deliver >>set_event
echo sched:sched_process_exit >>set_event

echo global >trace_clock
echo 40960 >buffer_size_kb
echo nop >current_tracer
echo 1 >tracing_on
