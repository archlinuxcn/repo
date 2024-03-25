#!/usr/bin/env bash

rm -f *.zip *.tar.gz

readonly ENGINE_VERSION="$(jq -r .engineRevision src/flutter/bin/cache/flutter.version.json)"

readonly MATERIAL_FONTS_VERSION="$(cat src/flutter/bin/internal/material_fonts.version | cut -d '/' -f4)"
readonly GRADLE_WRAPPER_VERSION="$(cat src/flutter/bin/internal/gradle_wrapper.version | cut -d '/' -f3)"
readonly LIBIMOBILEDEVICE_VERSION="$(cat src/flutter/bin/internal/libimobiledevice.version)"
readonly USBMUXD_VERSION="$(cat src/flutter/bin/internal/usbmuxd.version)"
readonly LIBPLIST_VERSION="$(cat src/flutter/bin/internal/libplist.version)"
readonly OPENSSL_VERSION="$(cat src/flutter/bin/internal/openssl.version)"
readonly IOS_DEPLOY_VERSION="$(cat src/flutter/bin/internal/ios-deploy.version)"

sed -i 's/_enginever=.*/_enginever='"${ENGINE_VERSION}"'/g' PKGBUILD
sed -i 's/_materialfontsver=.*/_materialfontsver='"${MATERIAL_FONTS_VERSION}"'/g' PKGBUILD
sed -i 's/_gradlewver=.*/_gradlewver='"${GRADLE_WRAPPER_VERSION}"'/g' PKGBUILD
