# Maintainer: Martchus <martchus@gmx.net>

# All my PKGBUILDs are managed at https://github.com/Martchus/PKGBUILDs where
# you also find the URL of a binary repository.

# if tests fail due to timeout, you can try to increase the timeout
# by setting SYNCTHING_TEST_TIMEOUT_FACTOR

# set the web view provider: either webkit, webengine, auto or none
_webview_provider=${SYNCTHING_TRAY_WEBVIEW_PROVIDER:-none}

# set the JavaScript provider: either script, qml, auto or none
_js_provider=${SYNCTHING_TRAY_JS_PROVIDER:-qml}

# set to non-empty string to enable KIO plugin to show Syncthing actions in
# Dolphin file browser
_enable_kio_plugin=${SYNCTHING_TRAY_ENABLE_KIO_PLUGIN:-0}

# set to non-empty string to enable Plasmoid for Plasma 5 desktop
_enable_plasmoid=${SYNCTHING_TRAY_ENABLE_PLASMOID:-0}

[[ $_enable_kio_plugin == 0 ]] && _enable_kio_plugin=
[[ $_enable_plasmoid == 0 ]] && _enable_plasmoid=

_reponame=syncthingtray
_cfg=qt6
pkgname=syncthingtray-$_cfg
_name=${pkgname%-$_cfg}
pkgver=1.1.3
pkgrel=1
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
pkgdesc='Tray application for Syncthing (using Qt 6)'
license=('GPL')
depends=('qtutilities-qt6' 'qt6-svg' 'openssl' 'desktop-file-utils' 'xdg-utils')
[[ $_webview_provider == none ]] && depends+=('qt6-base')
[[ $_webview_provider == webkit ]] && depends+=('qt6-webkit')
[[ $_webview_provider == webengine ]] && depends+=('qt6-webengine')
[[ $_js_provider == script ]] && depends+=('qt6-script')
[[ $_js_provider == qml ]] && depends+=('qt6-declarative')
[[ $_enable_kio_plugin ]] && optdepends+=('kio: KIO plugin for Syncthing actions in Dolphin')
[[ $_enable_plasmoid ]] && optdepends+=('plasma-workspace: Plasmoid for Plasma 6 desktop')
makedepends=('cmake' 'ninja' 'qt6-tools' 'clang' 'mesa')
checkdepends=('cppunit' 'syncthing' 'iproute2')
[[ $_enable_kio_plugin ]] && makedepends+=('kio')
[[ $_enable_plasmoid ]] && makedepends+=('plasma-framework' 'extra-cmake-modules')
url="https://github.com/Martchus/${_reponame}"
source=("${_name}-${pkgver}.tar.gz::https://github.com/Martchus/${_reponame}/archive/v${pkgver}.tar.gz")
sha256sums=('7e6580e8dee78fb3a3dacf4d55f02c7f8b44dac1785275bb7d937e59f57f295b')

ephemeral_port() {
  comm -23 <(seq 49152 65535) <(ss -tan | awk '{print $4}' | cut -d':' -f2 | grep "[0-9]\{1,5\}" | sort | uniq) | shuf | head -n 1
}

build() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"

  local additional_args=
  [[ $_enable_kio_plugin ]] || additional_args+=' -DNO_FILE_ITEM_ACTION_PLUGIN=ON'
  [[ $_enable_plasmoid ]] || additional_args+=' -DNO_PLASMOID=ON'

  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE:STRING='Release' \
    -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
    -DCONFIGURATION_NAME:STRING="$_cfg" \
    -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
    -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-$_cfg" \
    -DLIB_SYNCTHING_CONNECTOR_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGFILEITEMACTION_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DLIB_SYNCTHING_MODEL_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGPLASMOID_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGWIDGETS_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGCTL_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DSYNCTHINGTRAY_CONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DQT_PACKAGE_PREFIX:STRING='Qt6' \
    -DBUILTIN_TRANSLATIONS:BOOL=ON \
    -DBUILTIN_TRANSLATIONS_OF_QT:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DWEBVIEW_PROVIDER="${_webview_provider}" \
    -DJS_PROVIDER="${_js_provider}" \
    -DSYSTEMD_SUPPORT=ON \
    $additional_args \
    .
  ninja
}

check() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  SYNCTHING_PORT=$(ephemeral_port) SYNCTHING_TEST_TIMEOUT_FACTOR=3 ninja check
}

package() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  DESTDIR="${pkgdir}" ninja install
}
