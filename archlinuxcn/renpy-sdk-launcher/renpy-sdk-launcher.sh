#!/usr/bin/bash
# Ren'Py SDK Launcher
# Checks and installs SDK if missing, then launches renpy.sh

USER_SDK_DIR="${HOME}/.local/share/renpy-sdk"
SYSTEM_SDK_DIR="/usr/share/renpy-sdk"

notify() {
    local title="${1}"
    local message="${2}"

    if command -v notify-send >/dev/null && [ -n "${DISPLAY}" ]; then
        notify-send --urgency=normal --expire-time=0 --app-name="Ren'Py" --icon=renpy "${title}" "${message}"
    else
        echo "${title} - ${message}"
    fi
}

# Check if SDK needs installation
if [ ! -d "${USER_SDK_DIR}" ] || [ -z "$(ls -A "${USER_SDK_DIR}")" ]; then
    # Create the target directory
    mkdir -p "${USER_SDK_DIR}"

    # Find the SDK archive (should be only one, but we'll take the first if multiple)
    sdk_archive="$(find "${SYSTEM_SDK_DIR}" -name 'renpy-sdk-*.tar.bz2' -print -quit)"
    if [ -z "${sdk_archive}" ]; then
        notify "Ren'Py SDK" "Error: No Ren'Py SDK archive found in ${SYSTEM_SDK_DIR}"
        exit 1
    fi

    notify "Ren'Py SDK" "Extracting ${sdk_archive} to ${USER_SDK_DIR}..."

    # Extract the archive (strip the top-level directory)
    tar --extract --auto-compress --no-same-owner --verbose --file="${sdk_archive}" --directory="${USER_SDK_DIR}" --strip-components=1
    if [ "${?}" -ne 0 ]; then
        notify "Ren'Py SDK" "Error: Failed to extract SDK archive"
        exit 1
    fi

    notify "Ren'Py SDK" "Installation successful"
else
    echo "${USER_SDK_DIR} contains files"
fi

# Launch renpy.sh
if [ -f "${USER_SDK_DIR}/renpy.sh" ]; then
    echo "Launching Ren'Py..."
    exec "${USER_SDK_DIR}/renpy.sh" "${@}"
else
    notify "Ren'Py SDK" "Error: renpy.sh not found in ${USER_SDK_DIR}"
    exit 1
fi
