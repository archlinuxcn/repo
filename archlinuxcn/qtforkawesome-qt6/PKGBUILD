# Maintainer: Martchus <martchus@gmx.net>

# All my PKGBUILDs are managed at https://github.com/Martchus/PKGBUILDs where
# you also find the URL of a binary repository.

_reponame=qtforkawesome
_pkgver_forkawesome=1.2.0
_reponame_forkawesome=Fork-Awesome-$_pkgver_forkawesome
_cfg=qt6
pkgname=qtforkawesome-$_cfg
_name=${pkgname%-$_cfg}
pkgver=0.3.1
pkgrel=1
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
pkgdesc='Library that bundles ForkAwesome for use within Qt applications (using Qt 6)'
license=(GPL-2.0-or-later)
depends=('qt6-base')
makedepends=('cmake' 'ninja' 'perl-yaml-libyaml' 'qtutilities-qt6' 'qt6-declarative' 'clang')
optdepends=(
  'qt6-declarative: Qt Quick integration'
  "$_name-doc: API documentation"
)
provides=(libqtforkawesome-qt6.so libqtquickforkawesome-qt6.so)
url="https://github.com/Martchus/${_reponame}"
source=("${_name}-${pkgver}.tar.gz::https://github.com/Martchus/${_reponame}/archive/v${pkgver}.tar.gz"
        "${_reponame_forkawesome}::https://github.com/ForkAwesome/Fork-Awesome/archive/refs/tags/${_pkgver_forkawesome}.tar.gz")
sha256sums=('b797af12542c5a2c7d11025ffaf9bea2b5abc603cef57044cfc20d0f5e7c8587'
            '23fba5f191f204e0414c547bf4c9b10fd7ca42c151260e8f64698449a75fbdb3')

build() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE:STRING='Release' \
    -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
    -DCONFIGURATION_NAME:STRING="$_cfg" \
    -DCONFIGURATION_DISPLAY_NAME="" \
    -DCONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DCONFIGURATION_PACKAGE_SUFFIX_QTUTILITIES:STRING="-$_cfg" \
    -DQT_PACKAGE_PREFIX:STRING='Qt6' \
    -DBUILTIN_TRANSLATIONS:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DFORK_AWESOME_FONT_FILE="$srcdir/${_reponame_forkawesome}/fonts/forkawesome-webfont.woff2" \
    -DFORK_AWESOME_ICON_DEFINITIONS="$srcdir/${_reponame_forkawesome}/src/icons/icons.yml" \
    .
  ninja
}

check() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  QT_QPA_PLATFORM=offscreen ninja check
}

package() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  DESTDIR="${pkgdir}" ninja install
}
