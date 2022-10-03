# Maintainer: Mantas Mikulėnas <grawity@gmail.com>
pkgname=adcli
pkgver=0.9.2
pkgrel=1
pkgdesc="Active Directory account management tool"
arch=(i686 x86_64)
url="https://gitlab.freedesktop.org/realmd/adcli"
license=(GPL3)
depends=(cyrus-sasl-gssapi krb5 libldap)
makedepends=(docbook-xml docbook-xsl git xmlto)
_commit=8e88e3590a19006362ea8b8dfdc18bb88b3cb3b5
source=("git+https://gitlab.freedesktop.org/realmd/adcli.git#commit=$_commit")
sha256sums=('SKIP')
#source=("https://www.freedesktop.org/software/realmd/releases/$pkgname-$pkgver.tar.gz"
#        "https://www.freedesktop.org/software/realmd/releases/$pkgname-$pkgver.tar.gz.sig")
#sha256sums=('72f6db406e35d96de2bdc413a5ed69f28a4a735c08670c6556713c3f83921aa4'
#            'SKIP')
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
    --prefix=/usr           \
    --sbindir=/usr/bin      \
    --sysconfdir=/etc       ;
  make
}

package() {
  cd "$pkgname"
  make DESTDIR="$pkgdir" install
}

# vim: ts=2:sw=2:et
