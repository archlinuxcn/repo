# Maintainer: Toke Høiland-Jørgensen <toke@toke.dk>
_pkgname=cyrus-sasl-xoauth2
pkgname=${_pkgname}-git
pkgrel=1
pkgver=r24.36aabca54fd6
pkgdesc="XOAUTH2 mechanism plugin for cyrus-sasl"
arch=(x86_64)
url="https://github.com/moriyoshi/$_pkgname"
license=('MIT')
makedepends=('git')
depends=('libsasl')
provides=('cyrus-sasl-xoauth2')
conflicts=('cyrus-sasl-xoauth2')
source=(git+$url.git)
md5sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=12 HEAD)"
}

build() {
  cd "$_pkgname"
  ./autogen.sh
  ./configure --prefix=/usr
  make
}

check() {
  cd "$_pkgname"
  make check
}

package() {
  cd "$_pkgname"
  make DESTDIR="$pkgdir/" install
  install -Dm644 COPYING $pkgdir/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
