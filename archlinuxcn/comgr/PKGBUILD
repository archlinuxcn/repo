# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Compiler support library for ROCm LLVM'
pkgver=5.2.3
pkgrel=2
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=('rocm-device-libs')
makedepends=('rocm-cmake' 'rocm-llvm')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('36d67dbe791d08ad0a02f0f3aedd46059848a0a232c5f999670103b0410c89dc')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake \
    -Wno-dev \
    -S "$_dirname/lib/comgr" \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_PREFIX_PATH='/opt/rocm/llvm'
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
