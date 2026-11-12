# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=china-operator-ip-git
pkgver=0.3468.d16fd0bf
pkgrel=1
pkgdesc="IPv4 and IPv6 address lists for Chinese network operators"
arch=('any')
url="https://github.com/gaoyifan/china-operator-ip"
license=('MIT')
makedepends=('git')
source=("git+https://github.com/gaoyifan/china-operator-ip.git#branch=ip-lists")
sha512sums=('SKIP')

pkgver() {
  cd china-operator-ip
  echo 0.$(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
  cd china-operator-ip
  install -Dm644 *.txt -t "$pkgdir"/usr/share/china-operator-ip/
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}

# vim:set ts=2 sw=2 et:
