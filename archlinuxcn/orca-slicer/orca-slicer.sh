#!/bin/bash
DIR="/usr/lib/OrcaSlicer"
export LD_LIBRARY_PATH="$DIR/bin:$LD_LIBRARY_PATH"

# FIXME: OrcaSlicer segfault workarounds
# 1) OrcaSlicer will segfault on systems where locale info is not as expected (i.e. Holo-ISO arch-based distro)
export LC_ALL=C

if [ "$XDG_SESSION_TYPE" = "wayland" ] && [ "$ZINK_DISABLE_OVERRIDE" != "1" ]; then
    if command -v glxinfo >/dev/null 2>&1; then
        VENDOR=$(glxinfo | grep "OpenGL vendor string:" | sed 's/.*: //')
        RENDERER=$(glxinfo | grep "OpenGL renderer string:" | sed 's/.*: //')
        if echo "$VENDOR $RENDERER" | grep -qi "NVIDIA"; then
            if command -v nvidia-smi >/dev/null 2>&1; then
                DRIVER_VERSION=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader | head -n1)
                DRIVER_MAJOR=$(echo "$DRIVER_VERSION" | cut -d. -f1)
                [ "$DRIVER_MAJOR" -gt 555 ] && ZINK_FORCE_OVERRIDE=1
            fi
            if [ "$ZINK_FORCE_OVERRIDE" = "1" ]; then
                export __GLX_VENDOR_LIBRARY_NAME=mesa
                export __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json
                export MESA_LOADER_DRIVER_OVERRIDE=zink
                export GALLIUM_DRIVER=zink
                export WEBKIT_DISABLE_DMABUF_RENDERER=1
            fi
        fi
    fi
fi
exec "$DIR/orca-slicer" "$@"
