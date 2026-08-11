# Maintainer: Martchus <martchus@gmx.net>

# All my PKGBUILDs are managed at https://github.com/Martchus/PKGBUILDs where
# you also find the URL of a binary repository.

# if tests fail due to timeout, you can try to increase the timeout
# by setting SYNCTHING_TEST_TIMEOUT_FACTOR

# set the web view provider: either webengine, auto or none
_webview_provider=${SYNCTHING_TRAY_WEBVIEW_PROVIDER:-webengine}

# set the JavaScript provider: either script, qml, auto or none
_js_provider=${SYNCTHING_TRAY_JS_PROVIDER:-qml}

# enables KIO plugin to show Syncthing actions in Dolphin file browser
_enable_kio_plugin=${SYNCTHING_TRAY_ENABLE_KIO_PLUGIN:-1}

# enables Plasmoid for Plasma desktop
_enable_plasmoid=${SYNCTHING_TRAY_ENABLE_PLASMOID:-1}

# enables "modern" UI
_enable_quick_gui=${SYNCTHING_TRAY_ENABLE_QUICK_GUI:-1}

[[ $_enable_kio_plugin == 0 ]] && _enable_kio_plugin=
[[ $_enable_plasmoid == 0 ]] && _enable_plasmoid=
[[ $_enable_quick_gui == 0 ]] && _enable_quick_gui=

_reponame=syncthingtray
_cfg=qt6
pkgname=syncthingtray-$_cfg
_name=${pkgname%-$_cfg}
pkgver=2.1.4
pkgrel=1
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
pkgdesc='Tray application for Syncthing (using Qt 6)'
license=(GPL-2.0-or-later)
depends=('qtutilities-qt6' 'qtforkawesome-qt6' 'c++utilities' 'boost-libs' 'qt6-svg' 'openssl' 'desktop-file-utils')
optdepends=('gnome-shell-extension-appindicator: tray icon support for GNOME Shell')
[[ $_webview_provider == none ]] && depends+=('qt6-base')
[[ $_webview_provider == webengine ]] && depends+=('qt6-webengine')
[[ $_js_provider == qml || $_enable_quick_gui ]] && depends+=('qt6-declarative')
[[ $_enable_kio_plugin ]] && optdepends+=('kio: KIO plugin for Syncthing actions in Dolphin')
[[ $_enable_plasmoid ]] && optdepends+=('plasma-workspace: Plasmoid for Plasma 6 desktop')
makedepends=('cmake' 'ninja' 'qt6-tools' 'qt6-declarative' 'clang' 'boost')
checkdepends=('cppunit' 'syncthing' 'iproute2')
[[ $_enable_kio_plugin ]] && makedepends+=('kio')
[[ $_enable_plasmoid ]] && makedepends+=('libplasma' 'extra-cmake-modules')
url="https://github.com/Martchus/${_reponame}"
source=("${_name}-${pkgver}.tar.gz::https://github.com/Martchus/${_reponame}/archive/v${pkgver}.tar.gz")
sha256sums=('935143ffe94365551345ae5cf5b710539925bf48168b17360e94243a6e1a32d7')

ephemeral_port() {
  comm -23 <(seq 49152 65535) <(ss -tan | awk '{print $4}' | cut -d':' -f2 | grep "[0-9]\{1,5\}" | sort | uniq) | shuf | head -n 1
}

build() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"

  local additional_args=
  [[ $_enable_kio_plugin ]] || additional_args+=' -DNO_FILE_ITEM_ACTION_PLUGIN=ON'
  [[ $_enable_plasmoid ]] || additional_args+=' -DNO_PLASMOID=ON'
  [[ $_enable_quick_gui ]] && additional_args+=' -DQUICK_GUI=ON -DQUICK_GUI_CONTROLS_STYLE=dynamic'

  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE:STRING='Release' \
    -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
    -DCONFIGURATION_NAME:STRING="$_cfg" \
    -DCONFIGURATION_DISPLAY_NAME="" \
    -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-$_cfg" \
    -DLIB_SYNCTHING_CONNECTOR_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGFILEITEMACTION_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DLIB_SYNCTHING_MODEL_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGPLASMOID_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGWIDGETS_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGCTL_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGTRAY_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DQT_PACKAGE_PREFIX:STRING='Qt6' \
    -DKF_PACKAGE_PREFIX:STRING='KF6' \
    -DBUILTIN_TRANSLATIONS:BOOL=ON \
    -DBUILTIN_TRANSLATIONS_OF_QT:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DWEBVIEW_PROVIDER="${_webview_provider}" \
    -DJS_PROVIDER="${_js_provider}" \
    -DSYSTEMD_SUPPORT=ON \
    $additional_args \
    .
  # try again due to "/usr/include/c++/16.1.1/span:170:24: internal compiler error: Segmentation fault"
  ninja || ninja
}

check() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  # https://github.com/syncthing/syncthing/issues/8785
  export HOME="$(mktemp -p "$PWD" -d testhome.XXX)"
  export QT_QPA_PLATFORM=offscreen
  export SYNCTHING_PORT=$(ephemeral_port)
  export SYNCTHING_TEST_TIMEOUT_FACTOR=3
  ninja check || ninja check
}

package() {
  depends+=('libqtutilities-qt6.so' 'libqtforkawesome-qt6.so' 'libc++utilities.so' 'libboost_filesystem.so')

  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  DESTDIR="${pkgdir}" ninja install
}
