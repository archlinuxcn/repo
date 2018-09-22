# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
#
# This is based on AUR packages socat2. The original maintainer is:
# Maintainer: Stefan Haller <haliner@googlemail.com>
#
# The original PKGBUILD for socat in the official repository was written by:
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Juergen Hoetzel <juergen@archlinux.org>
# Contributor: John Proctor <jproctor@prium.net>

pkgname=socat2
_pkgname=socat
pkgver=2.0.0_b9
pkgrel=2
pkgdesc='Multipurpose relay, version 2 (development version)'
url='http://www.dest-unreach.org/socat/socat-version2.html'
license=('GPL2')
arch=('i686' 'x86_64')
depends=('readline' 'openssl-1.0')
makedepends=('yodl' 'git')
source=(
  http://www.dest-unreach.org/socat/download/socat-2.0.0-b9.tar.bz2
  sslv3.patch
)
sha256sums=('49efb0a5c66b94b279014addc2851faf8ebbd1ec4b7e31c1de7e912d7b4983d2'
            '3744575806f489ad0d3673e6a397badd4b61ecbd6e474ece67b347e13c5076b5')

prepare() {
  cd $_pkgname-${pkgver/_/-}

  patch -Np1 -i ../sslv3.patch
}

build() {
  cd $_pkgname-${pkgver/_/-}

  CPPFLAGS="$CPPFLAGS -I/usr/include/openssl-1.0" \
  LDFLAGS="$LDFLAGS -L/usr/lib/openssl-1.0" \
  ./configure --prefix=/usr

  make
}

package() {
  cd $_pkgname-${pkgver/_/-}

  make DESTDIR="$pkgdir" install

  # Make it co-installable with socat
  find "${pkgdir}/usr/bin/" -type f -executable -exec mv {} {}2 \;
  mv "$pkgdir"/usr/share/man/man1/socat{,2}.1
}
