# Maintainer: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: birdflesh <antkoul at gmail dot com>
# Contributor: Zephyr

_pkgbasename=oxygen-gtk2
pkgname=lib32-${_pkgbasename}
pkgver=1.4.0
pkgrel=1
pkgdesc="Port of the default KDE widget theme (Oxygen) to GTK2"
arch=('x86_64')
url="https://projects.kde.org/projects/playground/artwork/oxygen-gtk/"
license=('LGPL')
depends=('lib32-gtk2' "${_pkgbasename}" 'lib32-dbus-glib')
conflicts=('lib32-oxygen-gtk')
replaces=('lib32-oxygen-gtk')
makedepends=('cmake' 'gcc-multilib')
source=(http://download.kde.org/stable/${_pkgbasename}/${pkgver}/src/${_pkgbasename}-${pkgver}.tar.bz2)
md5sums=('ccc9e468a5ea04159ca2040ee3f434e1')

build() {
  mkdir build
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
