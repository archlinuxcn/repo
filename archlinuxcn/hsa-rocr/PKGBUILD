# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-rocr
pkgver=5.2.0
pkgrel=2
pkgdesc='ROCm Platform Runtime: ROCr a HPC market enhanced HSA based runtime'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCR-Runtime.html'
license=('custom:NCSAOSL')
depends=('libelf' 'hsakmt-roct' 'rocm-device-libs' 'hsa-amd-aqlprofile')
makedepends=('cmake' 'rocm-llvm' 'xxd')
provides=("rocr-runtime=$pkgver")
replaces=('rocr-runtime')
conflicts=('rocr-runtime')
_git='https://github.com/RadeonOpenCompute/ROCR-Runtime'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('529e49693dd9f6459586dd0a26f14dd77dbdf8c0b45fb54830b294eba7babd27')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_CXX_FLAGS='-DNDEBUG' \
        "$_dirname/src"
  make
}

package() {
  make DESTDIR="$pkgdir" install

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
    /opt/rocm/lib
    /opt/rocm/hsa/lib
EOF
}
