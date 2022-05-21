# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocminfo
pkgver=5.1.3
pkgrel=1
pkgdesc='ROCm info tools - rocm_agent_enumerator'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocminfo'
license=('custom:NCSAOSL')
depends=('pciutils' 'python' 'hsa-rocr')
makedepends=('cmake' 'git' 'rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "fix-kfd.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocminfo/pull/53.patch")
sha256sums=('7aecd7b189e129b77c8f2af70be2926a0f3a5ee89814879bc8477924a7e6f2ae'
            'SKIP')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 < "${srcdir}/fix-kfd.patch"
}

build() {
  # ROCRTST_BLD_TYPE=Release fixes a build error regarding _FORTIFY_SOURCE=2
  cmake -DCMAKE_PREFIX_PATH=/opt/rocm \
        -DROCRTST_BLD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_INSTALL_LIBDIR=lib \
        "$_dirname"
  make
}

package() {
  DESTDIR="$pkgdir" make install
  mkdir -p "$pkgdir/usr/bin"
  ln -st "$pkgdir/usr/bin" /opt/rocm/bin/rocminfo
  ln -st "$pkgdir/usr/bin" /opt/rocm/bin/rocm_agent_enumerator
}
