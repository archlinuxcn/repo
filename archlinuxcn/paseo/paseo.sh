#!/bin/sh
# Paseo wraps Electron with a Commander.js CLI that rejects Chromium flags,
# so we configure Ozone via the Electron-level env var instead (Electron 28+).
# Override by exporting ELECTRON_OZONE_PLATFORM_HINT before invocation.
export ELECTRON_OZONE_PLATFORM_HINT="${ELECTRON_OZONE_PLATFORM_HINT:-auto}"
# Launch the app directory (not dist/main.js directly): Electron's default_app
# reads package.json next to it, so app.getVersion() reports the real version
# instead of "0.0" — which the daemon manager would treat as a version
# mismatch and restart the user's daemon on every launch.
exec electron41 /usr/lib/paseo/packages/desktop "$@"
