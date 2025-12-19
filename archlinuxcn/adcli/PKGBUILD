# Maintainer: Mantas Mikulėnas <grawity@gmail.com>
pkgname=adcli
pkgver=0.9.3.1.r1.g9c31bb0
pkgrel=1
pkgdesc="Active Directory account management tool"
arch=(i686 x86_64)
url="https://gitlab.freedesktop.org/realmd/adcli"
license=(GPL3)
depends=(
  cyrus-sasl-gssapi
  krb5
  libldap
)
makedepends=(
  docbook-xml
  docbook-xsl
  git
  smbclient   # optional, for offline join support
  xmlto
)
source=("git+https://gitlab.freedesktop.org/realmd/adcli.git#commit=9c31bb06590f2d96a2d6d8ce87dc3273c283a671")
sha256sums=('bc7c82d1f81d57a508ddbe6345be8d9c7865fb62b963715e138b786b4d1b38e1')
validpgpkeys=('C0F67099B808FB063E2C81117BFB1108D92765AF')

pkgver() {
  cd "$pkgname"
  git describe --tags | sed "s/-/.r/; s/-/./"
}

prepare() {
  cd "$pkgname"
  autoreconf -fi
}

build() {
  cd "$pkgname"
  ./configure \
    --prefix=/usr             \
    --sbindir=/usr/bin        \
    --sysconfdir=/etc         \
    --disable-selinux-support ;
  make
}

package() {
  cd "$pkgname"
  make DESTDIR="$pkgdir" install
}

# vim: ts=2:sw=2:et
