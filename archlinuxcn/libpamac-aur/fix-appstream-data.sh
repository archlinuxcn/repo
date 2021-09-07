#!/bin/bash
tmp="/tmp/fix-appstream-data"
while read -r archive; do
        if [[ $(zcat "${archive}" | grep -cm1 '<em>') == "1" ]]; then
            zcat "${archive}"  | sed 's|<em>||g;s|<\/em>||g;s|<strong>||g;s|<\/strong>||g' | gzip > "${tmp}"
            cp "${tmp}" "${archive}"
            rm "${tmp}"
            echo "      archive ${archive} fixed"
        fi
done
