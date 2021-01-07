# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-rocr
pkgver=4.0.0
pkgrel=1
pkgdesc='ROCm Platform Runtime: ROCr a HPC market enhanced HSA based runtime'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCR-Runtime.html'
license=('custom:NCSAOSL')
depends=('libelf' 'hsakmt-roct' 'rocm-device-libs')
makedepends=('cmake' 'llvm-amdgpu' 'xxd')
provides=("rocr-runtime=$pkgver")
replaces=('rocr-runtime')
conflicts=('rocr-runtime')
_git='https://github.com/RadeonOpenCompute/ROCR-Runtime'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'remove-warnings.patch')
sha256sums=('e84c48e80ea38698a5bd5da3940048ad3cab3696d10a53132acad07ca357f17c'
            '9aecc193aafe58c235b82b7d7c4444fd4175224233fde6a23c54014b3dcc0f6a')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

prepare() {
  cd "$srcdir/$_dirname"
  patch -Np1 -i "$srcdir/remove-warnings.patch"
}

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
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
