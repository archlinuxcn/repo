# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsakmt-roct
pkgver=5.1.0
pkgrel=1
pkgdesc='Radeon Open Compute Thunk Interface'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/ROCt.html'
license=('MIT')
depends=('numactl' 'pciutils' 'libdrm')
makedepends=('cmake')
provides=("roct-thunk-interface=$pkgver")
replaces=('roct-thunk-interface')
_git='https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('032717e80b1aefed59f11399e575564ee86ee7c125e889f7c79c2afdfab1eb93')
options=(!lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm "$_dirname"
  make
}

package() {
  make DESTDIR="$pkgdir" install

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
    /opt/rocm/lib
EOF
}
