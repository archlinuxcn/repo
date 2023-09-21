# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: grimi <grimi at poczta dot fm>
# Contributor: Thomas Nordenmark <t.nordenmark@gmail.com>
# Contributor: Travis Nickles <nickles.travis@gmail.com>

pkgname=antimicrox
pkgver=3.3.4
pkgrel=3
pkgdesc="Graphical program used to map keyboard buttons and mouse controls to a gamepad"
arch=("aarch64" "arm" "armv6h" "armv7h" "i686" "x86_64")
url="https://github.com/AntiMicroX/${pkgname/x}X"
license=("GPL3")
depends=("hicolor-icon-theme" "libxtst" "qt5-base" "sdl2")
makedepends=("cmake" "extra-cmake-modules" "gettext" "itstool" "qt5-tools")
provides=("${pkgname/x}")
conflicts=("${pkgname/x}")
replaces=("${pkgname/x}")
_versionpart=-updated-SDL
source=("${pkgname}-${pkgver}${_versionpart}.tar.gz::https://github.com/AntiMicroX/${pkgname/x/X}/archive/${pkgver}${_versionpart}.tar.gz")
sha256sums=("4819d80e814e8315b49af3f89034b4428ab796e2e9cfc0dcbd0da96e387a5a5b")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}${_versionpart}"

  cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DUSE_SDL_2=ON \
    -DAPPDATA=ON \
    -DWITH_UINPUT=ON \
    -DWITH_X11=ON \
    -DWITH_XTEST=ON
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}${_versionpart}"
  make DESTDIR="${pkgdir}" install
}

