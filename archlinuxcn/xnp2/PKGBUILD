# Maintainer: Gustavo Alvarez Lopez <sl1pkn07@gmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr>
# Contributor: Score_Under <seejay.11@gmail.com>

pkgname=xnp2
pkgver=0.86
pkgrel=2
pkgdesc="X Neko Project II, a PC-9801 emulator"
arch=('i686' 'x86_64')
url='http://www.nonakap.org/np2'
license=('BSD')
depends=('gtk2'
         'sdl2_mixer'
         )
source=("http://www.nonakap.org/np2/release/xnp2-${pkgver}.tar.bz2"
        'patch.patch'
        )
sha256sums=('e0b8c93f54682a4b3373907fd9ffe78094f95f7430dffc5038eccbcc4c3f78fd'
            '03547eda251aa8678abcfb0f3780bec02deb16f3d326ac3cabaccd2d8fef7746'
            )

prepare() {
  mkdir -p build

  patch -d "xnp2-${pkgver}" -p1 -i "${srcdir}/patch.patch"

  cd build
  ../xnp2-${pkgver}/x11/configure \
    --prefix=/usr \
    --enable-build-all \
    --enable-ia32
    #--enable-gtk3
}

build() {
  make -C build
}

package() {
  make -C build DESTDIR="${pkgdir}/" install
}
