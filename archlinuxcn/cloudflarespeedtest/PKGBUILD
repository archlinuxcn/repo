# Maintainer: Tom Yang <tomyangsh at icloud dot com>

pkgname=cloudflarespeedtest
pkgver=2.2.4
pkgrel=2
license=('GPL3')
pkgdesc="Cloudflare IP Batch Test Tool"
makedepends=('go' 'git')
arch=('x86_64')
url="https://github.com/XIU2/CloudflareSpeedTest"
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
  cd "CloudflareSpeedTest"
  sed -i s@ip.txt@/usr/share/cloudflarespeedtest/ip.txt@g main.go
  sed -i s@ipv6.txt@/usr/share/cloudflarespeedtest/ipv6.txt@g main.go
  go build -ldflags="-s -w -X main.version=v$pkgver" -o $pkgname
}

package() {
  cd "CloudflareSpeedTest"
  install -Dm755 $pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm644 ip.txt "$pkgdir"/usr/share/cloudflarespeedtest/ip.txt
  install -Dm644 ipv6.txt "$pkgdir"/usr/share/cloudflarespeedtest/ipv6.txt
}
