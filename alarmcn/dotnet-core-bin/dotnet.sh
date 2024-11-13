# Set location for AppHost lookup
[ -z "$DOTNET_ROOT" ] && export DOTNET_ROOT=/usr/share/dotnet

# Add dotnet directory to PATH, according to docs it must be added, plus VSCode C# Dev Kit doesn't work without this.
# See https://learn.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual#set-environment-variables-system-wide
case "$PATH" in
    *"$DOTNET_ROOT"* ) true ;;
    * ) PATH="$PATH:$DOTNET_ROOT" ;;
esac

# Add dotnet tools directory to PATH
[ -z "$DOTNET_TOOLS_PATH" ] && export DOTNET_TOOLS_PATH="$HOME/.dotnet/tools"
case "$PATH" in
    *"$DOTNET_TOOLS_PATH"* ) true ;;
    * ) PATH="$PATH:$DOTNET_TOOLS_PATH" ;;
esac

# Extract self-contained executables under HOME to avoid multi-user issues from using the default '/var/tmp'
[ -z "$DOTNET_BUNDLE_EXTRACT_BASE_DIR" ] && export DOTNET_BUNDLE_EXTRACT_BASE_DIR="${XDG_CACHE_HOME:-"$HOME"/.cache}/dotnet_bundle_extract"
