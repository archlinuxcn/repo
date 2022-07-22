# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=5.2.1
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=(zlib rocm-device-libs)
makedepends=(cmake rocm-llvm rocm-cmake)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('ebeaea8e653fc2b9d67d3271be44690ac7876ee679baa01d47863e75362b8c85')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH="/opt/rocm/llvm;/opt/rocm" \
        "$_dirname/lib/comgr"

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
