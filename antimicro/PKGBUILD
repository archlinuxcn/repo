# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: grimi <grimi at poczta dot fm>
# Contributor: Thomas Nordenmark <t.nordenmark@gmail.com>
# Contributor: Travis Nickles <nickles.travis@gmail.com>

pkgname=antimicro
pkgver=2.24.1
pkgrel=2
pkgdesc="Graphical program used to map keyboard keys and mouse controls to a gamepad"
arch=("i686" "x86_64")
url="https://github.com/juliagoda/${pkgname}"
license=("GPL3")
depends=("desktop-file-utils" "hicolor-icon-theme" "libxtst" "qt5-base" "sdl2")
makedepends=("cmake" "extra-cmake-modules" "gettext" "itstool" "qt5-tools")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/juliagoda/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=("1a7f8693b2f969426a1ae1177af9d76389274308ae2f713a694df7c616369b31")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  cmake \
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

