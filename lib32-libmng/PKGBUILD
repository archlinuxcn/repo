# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Florian Pritz <flo [at] xssn [dot] at>

pkgname=lib32-libmng
pkgver=2.0.3
pkgrel=1
pkgdesc="A collection of routines used to create and manipulate MNG format graphics files (32-bit)"
arch=('x86_64')
url="http://www.libmng.com/"
license=('custom')
depends=('lib32-lcms2' "${pkgname#lib32-}" )
makedepends=('gcc-multilib')
source=(http://downloads.sourceforge.net/sourceforge/${pkgname#lib32-}/${pkgname#lib32-}-${pkgver}.tar.xz{,.asc})
sha512sums=('764efd94643c17c449abcb8f676ec2aa750a2461cf46bc961343f8d443a16ac2caa135c27d846deb2351b9f25d6170c42a500d21f63c13276905fdd743b8fec6'
            'SKIP')
validpgpkeys=('8048643BA2C840F4F92A195FF54984BFA16C640F')

build() {
  # Modify environment to generate 32-bit ELF. Respects flags defined in makepkg.conf
  export CFLAGS="-m32 ${CFLAGS}"
  export CXXFLAGS="-m32 ${CXXFLAGS}"
  export LDFLAGS="-m32 ${LDFLAGS}"
  export PKG_CONFIG_LIBDIR='/usr/lib32/pkgconfig'

  cd ${pkgname#lib32-}-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/lib32
  make
}

package() {
  cd ${pkgname#lib32-}-${pkgver}
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,include,share}
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
