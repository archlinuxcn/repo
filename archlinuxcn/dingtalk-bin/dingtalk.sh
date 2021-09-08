#!/bin/bash -e
cd /opt/dingtalk/release
LD_PRELOAD="/usr/lib/libnss3.so" ./com.alibabainc.dingtalk
