# Maintainer: Martchus <martchus@gmx.net>

# All my PKGBUILDs are managed at https://github.com/Martchus/PKGBUILDs where
# you also find the URL of a binary repository.

_reponame=qtutilities
_cfg=qt6
pkgname=qtutilities-$_cfg
_name=${pkgname%-$_cfg}
pkgver=6.3.3
pkgrel=1
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
pkgdesc='Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models (using Qt 6)'
license=('GPL')
depends=('c++utilities' 'qt6-base')
makedepends=('cmake' 'ninja' 'qt6-tools' 'clang' 'mesa')
optdepends=("$_name-doc: API documentation")
url="https://github.com/Martchus/${_reponame}"
source=("${_name}-${pkgver}.tar.gz::https://github.com/Martchus/${_reponame}/archive/v${pkgver}.tar.gz")
sha256sums=('7f9054cdabdbf6e0afd7f27ae8ced59121349b5fcf15ce2638b5aa852d46ab4a')

build() {
  cd "$srcdir/${PROJECT_DIR_NAME:-$_reponame-$pkgver}"
  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE:STRING='Release' \
    -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
    -DCONFIGURATION_NAME:STRING="$_cfg" \
    -DCONFIGURATION_DISPLAY_NAME="Qt 6" \
    -DCONFIGURATION_TARGET_SUFFIX:STRING="$_cfg" \
    -DQT_PACKAGE_PREFIX:STRING='Qt6' \
    -DBUILTIN_TRANSLATIONS:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
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
