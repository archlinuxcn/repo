#!/bin/bash -e
export LD_LIBRARY_PATH=/usr/lib/dingtalk:$LD_LIBRARY_PATH
cd /opt/dingtalk/release
./com.alibabainc.dingtalk
