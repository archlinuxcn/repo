# Maintainer: Mantas Mikulėnas <grawity@gmail.com>
pkgname=adcli
pkgver=0.9.3.1
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
source=("git+https://gitlab.freedesktop.org/realmd/adcli.git#tag=$pkgver")
sha256sums=('8fadd4a6df3f55134fc4b6458f7d0a3dd5ee5dd64a5150b89007077053b7c793')
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
