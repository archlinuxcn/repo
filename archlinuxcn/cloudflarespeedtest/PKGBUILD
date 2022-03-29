# Maintainer: Tom Yang <tomyangsh at icloud dot com>

pkgname=cloudflarespeedtest
pkgver=2.0.3
pkgrel=1
license=('GPL3')
pkgdesc="Cloudflare IP Batch Test Tool"
makedepends=('go')
conflicts=("cloudflarespeedtest")
arch=('x86_64')
url="https://github.com/XIU2/CloudflareSpeedTest"
source=("https://github.com/XIU2/CloudflareSpeedTest/archive/v${pkgver}.tar.gz"
	'patch.patch')
sha256sums=('SKIP'
	    'SKIP')

prepare() {
  cd "CloudflareSpeedTest-$pkgver"
  patch -p1 -i "$srcdir/patch.patch"
}

build() {
  cd "CloudflareSpeedTest-$pkgver"

  go build -o $pkgname
}

package() {
  cd "CloudflareSpeedTest-$pkgver"
  install -Dm755 $pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm644 ip.txt "$pkgdir"/usr/share/cloudflarespeedtest/ip.txt
  install -Dm644 ipv6.txt "$pkgdir"/usr/share/cloudflarespeedtest/ipv6.txt
}
