#!/bin/bash -e
cd /opt/apps/com.alibabainc.dingtalk/files/*-Release*/
LD_PRELOAD="/usr/lib/libnss3.so" ./com.alibabainc.dingtalk
