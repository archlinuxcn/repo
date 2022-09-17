# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocminfo
pkgver=5.2.3
pkgrel=2
pkgdesc='ROCm Application for Reporting System Info '
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocminfo'
license=('custom:NCSAOSL')
depends=('pciutils' 'python' 'hsa-rocr')
makedepends=('rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "fix-kfd.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocminfo/pull/53.patch")
sha256sums=('38fe8db21077100ee2242bd087371f6b8e0078d3a269e145d3a4ab314d0b8902'
            'SKIP')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 < "${srcdir}/fix-kfd.patch"
}

build() {
  # ROCRTST_BLD_TYPE=Release fixes a build error regarding _FORTIFY_SOURCE=2
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_PREFIX_PATH=/opt/rocm \
    -DROCRTST_BLD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_INSTALL_LIBDIR=lib
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
