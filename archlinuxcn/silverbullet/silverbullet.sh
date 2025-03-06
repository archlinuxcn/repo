#!/usr/bin/sh

set -eu

HOST=${HOST:-localhost}
PORT=${PORT:-3000}
echo >&2 "listening on $HOST:$PORT"

if [ $# -gt 1 ]; then
  echo >&2 "usage: $0 optional_path"
  exit 1
fi

if [ $# = 1 ]; then
  echo >&2 "overriding $DOCS with $1"
  DOCS=$1
fi

if [ -z "${DOCS:-}" ]; then
  echo >&2 'root directory not set in $DOCS'
  exit 1
fi

echo >&2 "using root directory $DOCS"
mkdir -p "$DOCS"

exec /usr/bin/deno run \
  --allow-all \
  --unstable-kv \
  --unstable-worker-options \
  /usr/lib/silverbullet/silverbullet.js \
  --hostname "$HOST" \
  --port "$PORT" \
  "$DOCS"
