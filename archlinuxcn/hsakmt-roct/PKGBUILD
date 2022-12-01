# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsakmt-roct
pkgver=5.4.0
pkgrel=1
pkgdesc='Radeon Open Compute Thunk Interface'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCt.html'
license=('MIT')
depends=('numactl' 'pciutils' 'libdrm')
makedepends=('cmake')
checkdepends=('rocm-llvm')
_git='https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('690a78a6e67ae2b3f518dbc4a1e267237d6a342e1063b31eef297f4a04d780f8')
options=(!lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake \
    -B build \
    -Wno-dev \
    -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=None \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build build
}

check() {
  local _tmpdir="$(mktemp -d -p $_dirname)"
  DESTDIR="$_tmpdir" cmake --install build

  LIBHSAKMT_PATH="$srcdir/$_tmpdir/opt/rocm" \
  cmake \
    -B kfd-build \
    -Wno-dev \
    -S "$_dirname/tests/kfdtest" \
    -DCMAKE_BUILD_TYPE=None \
    -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm \
    -DCMAKE_LINK_DIRECTORIES_BEFORE=ON
  cmake --build kfd-build

  cd kfd-build
  # Stress tests cause system crash,
  # https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/issues/76
  LD_LIBRARY_PATH="$srcdir/$_tmpdir/opt/rocm" \
  ./run_kfdtest.sh -e "KFDMemoryTest.LargestSysBufferTest:KFDMemoryTest.BigSysBufferStressTest:KFDQMTest.CreateQueueStressSingleThreaded"
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  echo '/opt/rocm/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
}
