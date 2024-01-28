# Maintainer: Tom Yang <tomyangsh at icloud dot com>

pkgname=cloudflarespeedtest
pkgver=2.2.5
pkgrel=2
license=('GPL-3.0-only')
pkgdesc="Cloudflare IP Batch Test Tool"
makedepends=('go')
arch=('x86_64')
url="https://github.com/XIU2/CloudflareSpeedTest"
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('9e120c31dadad329b54b5d87047db70bf16b5d3b82c45ccfaac02522cdb92fdf')

build() {
  cd "CloudflareSpeedTest-$pkgver"
  sed -i s@ip.txt@/usr/share/cloudflarespeedtest/ip.txt@g main.go
  sed -i s@ipv6.txt@/usr/share/cloudflarespeedtest/ipv6.txt@g main.go
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -ldflags="-X main.version=v$pkgver" -o $pkgname
}

package() {
  cd "CloudflareSpeedTest-$pkgver"
  install -Dm755 $pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm644 ip.txt "$pkgdir"/usr/share/cloudflarespeedtest/ip.txt
  install -Dm644 ipv6.txt "$pkgdir"/usr/share/cloudflarespeedtest/ipv6.txt
}
