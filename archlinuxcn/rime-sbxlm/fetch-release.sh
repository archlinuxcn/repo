#!/usr/bin/bash
variant=$1
prop=$2 # url or version

releases=$(curl -X GET --header 'Content-Type: application/json;chartset=UTF-8' 'https://gitee.com/api/v5/repos/sbxlm/sbxlm/releases/latest')
# switch prop
case $prop in
    url)
        download_url=$(echo $releases | jq -r ".assets[] | select(.name) | select(.name | contains(\"$variant\")) | .browser_download_url")
        echo $download_url
        ;;
    version)
        version=$(echo $releases | jq -r ".tag_name")
        echo $version
        ;;
    *)
        echo "Invalid property"
        exit 1
        ;;
esac


