# Maintainer: Gustavo Alvarez Lopez <sl1pkn07@gmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr>
# Contributor: Score_Under <seejay.11@gmail.com>

pkgname=xnp2
pkgver=0.86
pkgrel=1
pkgdesc="X Neko Project II, a PC-9801 emulator"
arch=('i686' 'x86_64')
url='http://www.nonakap.org/np2'
license=('BSD')
depends=('gtk2'
         'sdl2_mixer'
         )
source=("http://www.nonakap.org/np2/release/xnp2-${pkgver}.tar.bz2"
        'patch.patch')
sha1sums=('02ade03afe672cc18068e75374eecc26ec53e32e'
          'f0056b23ae5fdc2b435f16a4879e495c45807375')

prepare() {
  cd "xnp2-${pkgver}"
  patch -p1 -i "${srcdir}/patch.patch"
}

build() {
  cd "xnp2-${pkgver}/x11"
  ./configure \
    --prefix=/usr \
    --enable-build-all \
    #--enable-gtk3
  LC_ALL=C make
}

package() {
  make -C "xnp2-${pkgver}/x11" DESTDIR="${pkgdir}/" install
}
