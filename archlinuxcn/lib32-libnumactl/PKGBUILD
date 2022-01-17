# Mantainer: ObserverOfTime <chronobserver@disroot.org>
# based on lib32-numactl

_basename=numactl
pkgname=lib32-libnuma
pkgver=2.0.14
pkgrel=3
pkgdesc='Simple NUMA policy support 32-bit version. Libraries only'
arch=('x86_64')
url='https://github.com/numactl/numactl'
license=('LGPL2.1' 'GPL2')
depends=('perl' 'numactl' 'lib32-gcc-libs')
conflicts=('lib32-numactl')
provides=("lib32-numactl=${pkgver}")
source=("$url/releases/download/v${pkgver}/${_basename}-${pkgver}.tar.gz")
sha256sums=('826bd148c1b6231e1284e42a4db510207747484b112aee25ed6b1078756bcff6')

build() {
  cd "$srcdir/$_basename-${pkgver/_/-}"
  export CC='gcc -m32' CXX='g++ -m32' \
         PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
  ./configure \
    --prefix=/usr \
    --libdir=/usr/lib32 \
    --host=i686-unknown-linux-gnu
  make
}

package() {
  cd "$srcdir/$_basename-${pkgver/_/-}"
  make DESTDIR="$pkgdir" install
  rm -rf "$pkgdir"/usr/{share,bin,include}
}
