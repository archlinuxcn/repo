# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocminfo
pkgver=4.0.0
pkgrel=1
pkgdesc='ROCm info tools - rocm_agent_enumerator'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocminfo'
license=('custom:NCSAOSL')
depends=('pciutils' 'python' 'hsa-rocr')
makedepends=('cmake' 'rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('0b3d692959dd4bc2d1665ab3a838592fcd08d2b5e373593b9192ca369e2c4aa7')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_PREFIX_PATH=/opt/rocm \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DROCM_DIR=/opt/rocm \
        "$_dirname"
  make
}

package() {
  DESTDIR="$pkgdir" make install
  mkdir -p "$pkgdir/usr/bin"
  ln -st "$pkgdir/usr/bin" /opt/rocm/bin/rocminfo
}
