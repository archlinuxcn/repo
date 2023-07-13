# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: grimi <grimi at poczta dot fm>
# Contributor: Thomas Nordenmark <t.nordenmark@gmail.com>
# Contributor: Travis Nickles <nickles.travis@gmail.com>

pkgname=antimicrox
pkgver=3.3.4
pkgrel=1
pkgdesc="Graphical program used to map keyboard buttons and mouse controls to a gamepad"
arch=("aarch64" "arm" "armv6h" "armv7h" "i686" "x86_64")
url="https://github.com/AntiMicroX/${pkgname/x}X"
license=("GPL3")
depends=("hicolor-icon-theme" "libxtst" "qt5-base" "sdl2")
makedepends=("cmake" "extra-cmake-modules" "gettext" "itstool" "qt5-tools")
provides=("${pkgname/x}")
conflicts=("${pkgname/x}")
replaces=("${pkgname/x}")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/AntiMicroX/${pkgname/x/X}/archive/${pkgver}.tar.gz")
sha256sums=("c5e8d7c827f64b0a162133f9cac2ddc8dc0c9243541fae1a8ced5424b4fb7b3c")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

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
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

