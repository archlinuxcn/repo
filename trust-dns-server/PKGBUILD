# Maintainer: Daniel M. Capella <polycitizen@gmail.com>

pkgname=trust-dns-server
pkgver=0.14.0
pkgrel=1
pkgdesc='Safe and secure DNS server with DNSec support'
arch=('x86_64')
url=http://trust-dns.org
license=('Apache')
depends=('openssl')
makedepends=('rust')
source=("$pkgname-$pkgver.tar.gz::https://crates.io/api/v1/crates/$pkgname/$pkgver/download")
sha512sums=('3b22bbf1cd2fc2629ad4ec569df9b8fcbf4d390d0e07012eafd22efcc358b59e6a18eadfa32e6a478b298e4152c539e659712704981856d59f0f11f54cd82cef')

build() {
  cd $pkgname-$pkgver
  cargo build --release
}

package() {
  cd $pkgname-$pkgver
  install -Dm755 target/release/named "$pkgdir"/usr/bin/named
}

# vim:set ts=2 sw=2 et:
