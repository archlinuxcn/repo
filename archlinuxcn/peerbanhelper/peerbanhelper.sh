#!/bin/sh
# Wrapper to start PeerBanHelper with the packaged layout.
set -euo pipefail

APP_DIR=/usr/share/java/peerbanhelper
JAVA_BIN=${PEERBANHELPER_JAVA_BIN:-/usr/bin/java}

exec "${JAVA_BIN}" \
  --enable-native-access=ALL-UNNAMED \
  -XX:+UseCompactObjectHeaders \
  -Dpbh.release=arch \
  -Dpbh.datadir="${PEERBANHELPER_DATADIR:-/var/lib/peerbanhelper}" \
  -Dpbh.configdir="${PEERBANHELPER_CONFIGDIR:-/var/lib/peerbanhelper/config}" \
  -Dpbh.logsdir="${PEERBANHELPER_LOGSDIR:-/var/log/peerbanhelper}" \
  -Dpbh.log.level="${PEERBANHELPER_LOG_LEVEL:-WARN}" \
  -Djdk.attach.allowAttachSelf=true \
  -XX:MaxRAMPercentage="${PEERBANHELPER_MAX_RAM_PERCENT:-85.0}" \
  -XX:SoftMaxHeapSize="${PEERBANHELPER_SOFT_MAX_HEAP:-386M}" \
  -XX:+UseG1GC \
  -XX:G1PeriodicGCInterval="${PEERBANHELPER_G1_PERIODIC_GC_INTERVAL:-60000}" \
  -XX:MaxHeapFreeRatio="${PEERBANHELPER_MAX_HEAP_FREE_RATIO:-15}" \
  -XX:MinHeapFreeRatio="${PEERBANHELPER_MIN_HEAP_FREE_RATIO:-5}" \
  -Xss512k \
  -XX:+UseStringDeduplication \
  -XX:-ShrinkHeapInSteps \
  ${PEERBANHELPER_JAVA_OPTS:-} \
  -jar "${APP_DIR}/PeerBanHelper.jar" \
  ${PEERBANHELPER_OPTS:-} \
  "$@"
