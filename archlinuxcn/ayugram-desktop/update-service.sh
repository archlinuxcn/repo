#!/usr/bin/bash

# Parse .SRCINFO and generate _service file for Open Build Service
# Requirements:
#   yq jq grep sort cut
# NOTE: yq is https://github.com/kislyuk/yq

set -e

declare -a services=()
declare source_line services_string
while read -r source_line
do
    shopt -s extglob
    source_line=${source_line##*( )} # Remove leading space
    source_line=${source_line%%*( )} # Remove tailing space
    shopt -u extglob
    declare filename="${source_line%%::*}" url="${source_line#*::}" service_params
    declare -a params
    params=("$(jq -rc --null-input '$ARGS.named' --arg '@name' 'url' --arg '#text' "$url")")
    if [[ -n "$filename" ]]
    then
        params+=("$(jq -rc --null-input '$ARGS.named' --arg '@name' 'filename' --arg '#text' "$filename")")
    fi
    service_params="$(jq -rc --null-input '$ARGS.positional' --jsonargs "${params[@]}")"
    services+=("$(jq -rc --null-input '$ARGS.named' --arg '@name' 'download_url' --argjson 'param' "$service_params")")
done < <(grep source .SRCINFO | sort -u | cut -d = -f 2)

services_string="$(jq -rc --null-input '$ARGS.positional' --jsonargs "${services[@]}")"
jq -rc --null-input '$ARGS.named' --argjson 'service' "$services_string" | yq -r . -x --xml-root 'services' > _service
