# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-rocr
pkgver=5.3.3
pkgrel=2
pkgdesc='HSA Runtime API and runtime for ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCR-Runtime.html'
license=('custom:NCSAOSL')
depends=('libelf' 'hsakmt-roct' 'rocm-device-libs')
makedepends=('cmake' 'rocm-llvm' 'xxd')
_git='https://github.com/RadeonOpenCompute/ROCR-Runtime'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('aca88d90f169f35bd65ce3366b8670c7cdbe3abc0a2056eab805d0192cfd7130')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname/src" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_FLAGS='-DNDEBUG' \
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
