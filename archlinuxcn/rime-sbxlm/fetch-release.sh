#!/usr/bin/bash
variant=WIN
sub_command=$1

case $sub_command in
    # retrieve the latest tag
    latest-tag)
        # echo in green to stderr
        echo -e "\033[0;32mRetrieving latest tag...\033[0m" >&2
        latests_json=$(curl -X GET --header 'Content-Type: application/json;chartset=UTF-8' 'https://gitee.com/api/v5/repos/sbxlm/sbxlm/releases/latest')
        tag=$(echo $latests_json | jq -r ".tag_name")
        echo $tag
        ;;
    # retrieve the sbxlm assets with the given tag
    url)
        tag_name=$2
        echo -e "\033[0;32mRetrieving assets for tag $tag_name...\033[0m" >&2
        resp=$(curl -X GET --header 'Content-Type: application/json;chartset=UTF-8' "https://gitee.com/api/v5/repos/sbxlm/sbxlm/releases/tags/$tag_name")
        download_url=$(echo $resp | jq -r ".assets[] | select(.name) | select(.name | contains(\"$variant\")) | .browser_download_url")
        echo $download_url
        ;;
    *)
        # show usage
        echo "Usage: fetch-release.sh latest-tag"
        echo "Usage: fetch-release.sh url <tag>"
        exit 1
        ;;
esac


