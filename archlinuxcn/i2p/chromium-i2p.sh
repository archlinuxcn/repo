#!/usr/bin/env bash
set -e

DATADIR=${XDG_CONFIG_HOME:-$HOME/.config}/chromium-i2p

[[ ! -f $DATADIR/.config ]] && {
    echo "creating config..."
    install -dm700 "$DATADIR"
    cat <<< '
CACHEDIR=/dev/shm/chromium-i2p # store in ram, or
#CACHEDIR=$DATADIR/.tmp        # keep on disk
CACHESIZE=128000000            # cache size in bytes

INCOGNITO=--incognito          # comment out if you wish to have
                               # urlhistory, passwords, etc. saved
PROXY=127.0.0.1:4444
CONSOLE=127.0.0.1:7657
' >"$DATADIR/.config"
    echo "$DATADIR/.config"
}

source "$DATADIR/.config"

/usr/bin/chromium "$INCOGNITO" \
    --user-data-dir="$DATADIR" \
    --disk-cache-dir="$CACHEDIR" \
    --disk-cache-size="$CACHESIZE" \
    --proxy-server="$PROXY" \
    --proxy-bypass-list=127.0.0.1,localhost \
    --{connectivity-check,gcm-checkin,gcm-registration,crash-server,google-apis,google-base,override-metrics-upload,realtime-reporting,test-logging}-url="http://0.0.0.0" \
    --disable-3d-apis \
    --disable-account-consistency \
    --disable-background-networking \
    --disable-breakpad \
    --disable-bundled-ppapi-flash \
    --disable-client-side-phishing-detection \
    --disable-cloud-import \
    --disable-default-apps \
    --disable-domain-reliability \
    --disable-file-system \
    --disable-logging \
    --disable-notifications \
    --disable-ntp-popular-sites \
    --disable-reading-from-canvas \
    --disable-remote-fonts \
    --disable-speech-api \
    --disable-sync \
    --disable-translate \
    --disable-voice-input \
    --enable-low-end-device-mode \
    --enable-strict-mixed-content-checking \
    --force-dark-mode \
    --no-default-browser-check \
    --no-pings \
    --no-report-upload \
    --site-per-process \
    --use-fake-device-for-media-stream \
   "${@:-$CONSOLE}"
