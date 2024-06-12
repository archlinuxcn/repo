#!/usr/bin/env bash

makepkg -ofC

readonly ENGINE_VERSION="$(cat src/flutter/bin/internal/engine.version)"

readonly MATERIAL_FONTS_VERSION="$(cat src/flutter/bin/internal/material_fonts.version | cut -d '/' -f4)"
readonly GRADLE_WRAPPER_VERSION="$(cat src/flutter/bin/internal/gradle_wrapper.version | cut -d '/' -f3)"
readonly LIBIMOBILEDEVICE_VERSION="$(cat src/flutter/bin/internal/libimobiledevice.version)"
readonly USBMUXD_VERSION="$(cat src/flutter/bin/internal/usbmuxd.version)"
readonly LIBPLIST_VERSION="$(cat src/flutter/bin/internal/libplist.version)"
readonly OPENSSL_VERSION="$(cat src/flutter/bin/internal/openssl.version)"
readonly IOS_DEPLOY_VERSION="$(cat src/flutter/bin/internal/ios-deploy.version)"
readonly SDK_STRING="$(grep sdk src/flutter/packages/flutter_tools/pubspec.yaml | awk -F "'" '{print $2}')"
readonly SDK_MIN="$(echo $SDK_STRING | awk -F '=' '{print $2}' | awk -F '-' '{print $1}')"
readonly SDK_MAX="$(echo $SDK_STRING | awk -F '<' '{print $2}' | awk -F '-' '{print $1}')"

# currently disabled since the constraints in upstream are not perfectly correct
# sed -i 's/_dartver=.*/_dartver=('"${SDK_MIN}"' '"${SDK_MAX}"')/g' PKGBUILD
sed -i 's/_enginever=.*/_enginever='"${ENGINE_VERSION}"'/g' PKGBUILD
sed -i 's/_materialfontsver=.*/_materialfontsver='"${MATERIAL_FONTS_VERSION}"'/g' PKGBUILD
sed -i 's/_gradlewver=.*/_gradlewver='"${GRADLE_WRAPPER_VERSION}"'/g' PKGBUILD
