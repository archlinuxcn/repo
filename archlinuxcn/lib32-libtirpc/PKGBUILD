# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: jtts <jussaar@mbnet.fi>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Franco Tortoriello <franco.tortoriello@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgname=lib32-libtirpc
pkgver=1.3.7
pkgrel=1
pkgdesc='Transport Independent RPC library (SunRPC replacement)'
arch=(x86_64)
url=https://git.linux-nfs.org/?p=steved/libtirpc.git;a=summary
license=('BSD-3-Clause')
depends=(
  lib32-glibc
  lib32-krb5
  libtirpc
)
makedepends=(git)
_tag=5bd87617e4b3129e76e79847c95bdea4b1290d9f
source=(git://git.linux-nfs.org/projects/steved/libtirpc.git#tag=${_tag})
b2sums=('62390a1330f5fb8f38e1c9c8096355393fe8c99a5290fe0c7b1c70472f97a2a3f621882596c9cb8d830f34e83d305e6c7a9a4a6809e0c9fc3aa3e3fc738765bf')

prepare() {
  cd libtirpc
  # git cherry-pick -n d473f1e1f6ba80bfaee4daa058da159305167323 # gcc 15
  # git cherry-pick -n 240ee6c774729c9c24812aa8912f1fcf8996b162 # gcc 15
  chmod +x autogen.sh
  ./autogen.sh
}

pkgver() {
  cd libtirpc
  git describe --tags | sed 's/libtirpc-//; s/-/./g'
}

build() {
  cd libtirpc
  export CC='gcc -m32'
  export PKG_CONFIG_PATH=/usr/lib32/pkgconfig
  ./configure \
    --prefix=/usr \
    --libdir=/usr/lib32 \
    --sysconfdir=/etc
  make
}

package() {
  cd libtirpc
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/{etc,usr/{include,share}}
  install -dm 755 "${pkgdir}"/usr/share/licenses/lib32-libtirpc
  install -m 644 COPYING -t "${pkgdir}"/usr/share/licenses/lib32-libtirpc/
}

# vim: ts=2 sw=2 et:
