# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=5.1.3
pkgrel=1
pkgdesc='Radeon Open Compute - device libs'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=(cmake rocm-cmake rocm-llvm)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('c41958560ec29c8bf91332b9f668793463904a2081c330c0d828bf2f91d4f04e')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    CC=/opt/rocm/llvm/bin/clang \
    cmake   -DCMAKE_INSTALL_PREFIX=/opt/rocm \
            -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm \
            "$_dirname"
    make
}

package() {
    DESTDIR="$pkgdir" make install
    install -Dm644 "$_dirname/LICENSE.TXT" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
