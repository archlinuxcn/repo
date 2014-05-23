# Upstream Maintainer: Bill Fraser <wfraser@codewise.org>
# Contributor: Felipe Contreras <felipe.contreras@gmail.com>
# Contributor: jtts
#
# From flex's PKGBUILD:
#   Maintainer: Allan McRae <allan@archlinux.org>
#   Contributor: judd <jvinet@zeroflux.org>
#
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=flex
pkgname=libx32-flex
pkgver=2.5.39
pkgrel=1
pkgdesc="A tool for generating text-scanning programs"
arch=('x86_64')
url="http://flex.sourceforge.net"
license=('custom')
groups=('base-devel')
depends=('libx32-glibc' 'm4' 'sh' $_pkgbasename)
options=(libtool staticlibs)
makedepends=('gcc-multilib-x32')
source=(http://downloads.sourceforge.net/sourceforge/flex/flex-$pkgver.tar.bz2 
        flex-2.5.38-no-bison.patch
        lex.sh)
sha256sums=('add2b55f3bc38cb512b48fad7d72f43b11ef244487ff25fc00aabec1e32b617f'
            '5ee23f97533c991b82e2aadc06d4682d7d05d99ee2abaf1ef9a82225ba9d0858'
            '9d03016a7c4ae1adb051f50f94407b3d7dee9d55924b5c1904261c9f0c1f86f6')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export LD="ld -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd $srcdir/$_pkgbasename-$pkgver

# These are no longer needed!
#  patch -Np1 -i $srcdir/flex-2.5.35-gcc44.patch
#  patch -Np1 -i $srcdir/flex-2.5.35-hardening.patch
#  patch -Np1 -i $srcdir/flex-2.5.35-missing-prototypes.patch

  patch -Np1 -i $srcdir/flex-2.5.38-no-bison.patch

  ./configure --prefix=/usr --libdir=/usr/libx32 \
    --mandir=/usr/share/man --infodir=/usr/share/info
  make
}

check() {
  cd $srcdir/$_pkgbasename-$pkgver
  make check
}

package() {
  cd $srcdir/$_pkgbasename-$pkgver

  make prefix=$pkgdir/usr \
    mandir=$pkgdir/usr/share/man \
    infodir=$pkgdir/usr/share/info \
    libdir=$pkgdir/usr/libx32 \
    install

  rm -rf "${pkgdir}"/usr/{include,share,bin}

  mkdir -p $pkgdir/usr/share/licenses
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

