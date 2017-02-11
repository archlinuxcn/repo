# Maintainer: Felix Yan <felixonmars@gmail.com>

_pkgname=dnsmasq-china-list
pkgname=$_pkgname-git
pkgver=0.36123.d366bf470
pkgrel=1
pkgdesc="Configuration for hot China domains to accelerate via Dnsmasq"
arch=('any')
url="https://github.com/felixonmars/dnsmasq-china-list"
license=('WTFPL') 
depends=('dnsmasq')
makedepends=('git')
source=("git://github.com/felixonmars/${_pkgname}.git")
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  echo 0.$(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
  install -Dm644 "$srcdir/$_pkgname/accelerated-domains.china.conf" "$pkgdir/etc/dnsmasq.d/accelerated-domains.china.conf"
  install -Dm644 "$srcdir/$_pkgname/bogus-nxdomain.china.conf" "$pkgdir/etc/dnsmasq.d/bogus-nxdomain.china.conf"
  install -Dm755 "$srcdir/$_pkgname/dnsmasq-update-china-list" "$pkgdir/usr/bin/dnsmasq-update-china-list"
}

# vim:set ts=2 sw=2 et:
