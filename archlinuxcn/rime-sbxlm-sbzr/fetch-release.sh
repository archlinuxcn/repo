#!/usr/bin/bash
curl -X GET --header 'Content-Type: application/json;charset=UTF-8' 'https://gitee.com/api/v5/repos/sbxlm/sbxlm/releases/latest' -o releases.json

