#!/usr/bin/bash
variant=$1

releases=$(curl -X GET --header 'Content-Type: application/json;chartset=UTF-8' 'https://gitee.com/api/v5/repos/sbxlm/sbxlm/releases/latest')
echo $releases | jq -r ".assets[] | select(.name) | select(.name | contains(\"$variant\")) | .browser_download_url"
