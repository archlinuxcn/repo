# Maintainer: Daniel M. Capella <polycitizen@gmail.com>

pkgname=trust-dns-server
pkgver=0.15.0
pkgrel=1
pkgdesc='Safe and secure DNS server with DNSec support'
arch=('x86_64')
url=http://trust-dns.org
license=('Apache')
depends=('openssl')
makedepends=('rust')
source=("$pkgname-$pkgver.tar.gz::https://crates.io/api/v1/crates/$pkgname/$pkgver/download")
sha512sums=('c45eb9e0dddcbe73f784a9334a4c8ae7bc4235b55897fc1b439296d792399d27c1e6d973ac88f295f67d7000a8d34e3e1abb3d90b582d3d8e820bfe5d288d978')

build() {
  cd $pkgname-$pkgver
  cargo build --release
}

package() {
  cd $pkgname-$pkgver
  install -Dm755 target/release/named "$pkgdir"/usr/bin/named
}

# vim:set ts=2 sw=2 et:
