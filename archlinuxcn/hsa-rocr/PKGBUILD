# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-rocr
pkgver=5.4.0
pkgrel=1
pkgdesc='HSA Runtime API and runtime for ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCR-Runtime.html'
license=('custom:NCSAOSL')
depends=('libelf' 'hsakmt-roct' 'rocm-device-libs')
makedepends=('cmake' 'rocm-llvm' 'xxd')
_git='https://github.com/RadeonOpenCompute/ROCR-Runtime'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('476cd18500cc227d01f6b44c00c7adc8574eb8234b6b4daefc219650183fa090')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"
options=(!lto)

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname/src" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_PREFIX_PATH=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  echo "/opt/rocm/hsa/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
}
