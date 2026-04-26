#!/usr/bin/env bash
set -euo pipefail

source PKGBUILD

REPO_URL="https://github.com/ONLYOFFICE/DesktopEditors.git"
REPO_DIR="DesktopEditors"


if [ ! -d "$REPO_DIR/.git" ]; then
    echo "[+] Cloning DesktopEditors..."
    git clone "$REPO_URL"
fi

cd "$REPO_DIR"

git fetch --all --tags
git checkout "v$pkgver"

# Iterate through submodules
git submodule status | while read -r line; do
    # Format: -<commit> <path>
    commit=$(echo "$line" | awk '{print $1}' | sed 's/^[-+]//')
    path=$(echo "$line" | awk '{print $2}')
    name=$(basename "$path")

    # Map repo name to your pkgname-* style
    case "$name" in
        core)                pkg="\$pkgname-core" ;;
        desktop-apps)        pkg="\$pkgname-desktop-apps" ;;
        desktop-sdk)         pkg="\$pkgname-desktop-sdk" ;;
        dictionaries)        pkg="\$pkgname-dictionaries" ;;
        sdkjs)               pkg="\$pkgname-sdkjs" ;;
        sdkjs-forms)         pkg="\$pkgname-sdkjs-forms" ;;
        web-apps)            pkg="\$pkgname-web-apps" ;;
        build_tools)         pkg="\$pkgname-build_tools" ;;
        core-fonts)          pkg="\$pkgname-core-fonts" ;;
        document-templates)  pkg="\$pkgname-document-templates" ;;
        onlyoffice.github.io) pkg="onlyoffice.github.io" ;;
        *)
            pkg="\$pkgname-$name"
            ;;
    esac

    echo "    \"$pkg::git+\${_url}/$name#commit=$commit\""
done

