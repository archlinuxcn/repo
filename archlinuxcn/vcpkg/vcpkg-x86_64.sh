# Disable vcpkg telemetry by default.
if [ -z "$VCPKG_DISABLE_METRICS" ]; then
    export VCPKG_DISABLE_METRICS="1"
fi

# Export the correct vcpkg root directory.
if [ -z "$VCPKG_ROOT" ]; then
    export VCPKG_ROOT="$HOME/.local/share/vcpkg"
fi
