# Maintainer: peeweep at 0x0 dot ee
# Contributor: Luca Weiss <luca (at) z3ntu (dot) xyz>
# Contributor: Johannes Dewender  arch at JonnyJD dot net
# Contributor: Bartosz Feński <fenio@debian.org>

pkgname=dh-make
pkgver=2.202102
pkgrel=2
pkgdesc="Tool that converts source archives into Debian package source"
arch=('any')
url="https://salsa.debian.org/debian/dh-make"
license=('GPL')
depends=('dpkg' 'make' 'python')
makedepends=('git')
source=("git+$url.git#tag=debian/$pkgver")
sha512sums=('SKIP')

package() {
  cd "$srcdir/$pkgname"
  install -D dh_make.py "$pkgdir"/usr/bin/dh_make
  install -d "$pkgdir"/usr/share/debhelper/dh_make
  cp -a lib/* "$pkgdir"/usr/share/debhelper/dh_make/
  install -Dm644 dh_make.1 "$pkgdir"/usr/share/man/man8/dh_make.8
}

# vim:set ts=2 sw=2 et:
