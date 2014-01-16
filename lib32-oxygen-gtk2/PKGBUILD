# Maintainer: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: birdflesh <antkoul at gmail dot com>
# Contributor: Zephyr

_pkgbasename=oxygen-gtk2
pkgname=lib32-${_pkgbasename}
pkgver=1.4.1
pkgrel=2
pkgdesc="Port of the default KDE widget theme (Oxygen) to GTK2"
arch=('x86_64')
url="https://projects.kde.org/projects/playground/artwork/oxygen-gtk/"
license=('LGPL')
depends=('lib32-gtk2' "${_pkgbasename}")
conflicts=('lib32-oxygen-gtk')
replaces=('lib32-oxygen-gtk')
makedepends=('cmake' 'gcc-multilib')
source=(http://download.kde.org/stable/${_pkgbasename}/${pkgver}/src/${_pkgbasename}-${pkgver}.tar.bz2)
md5sums=('27bb5826d936fe2bddab35057739908f')

prepare() {
  mkdir build
}

build() {
  cd build

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cmake ../${_pkgbasename}-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DINSTALL_PATH_GTK_ENGINES=/usr/lib32/gtk-2.0/2.10.0/engines
  make
}

package() {
  cd build
  make DESTDIR=${pkgdir} install

  # Clean up directories provided by x86_64 package
  rm -rf ${pkgdir}/usr/bin
  rm -rf ${pkgdir}/usr/share
}
