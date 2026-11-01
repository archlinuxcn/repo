# Maintainer: w0rty <mawo97 at gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>

pkgname=wails
pkgver=3.1.0 # renovate: datasource=github-tags depName=wailsapp/wails
pkgrel=1
pkgdesc="Create desktop apps using Go and Web Technologies"
arch=(x86_64)
url="https://github.com/wailsapp/wails"
license=(MIT)
depends=('glibc' 'npm' 'gtk4' 'webkitgtk-6.0')
makedepends=('go')
optdepends=('docker')
source=($url/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('5fe5fa3b12df314a4b4d6cd1fe045c6b79a45c4e1463b80830d11da6b4d53678a9cfb8d36823c948d6296333cb8da41a91a2daaddc68abcf07760b674c179a94')
b2sums=('18d3d1ae00fd66f74fe47f0749d8c508b87b0c30e2d80de3d5e0f012e24da7adf49e7b5d78a2573d6e6777f3277aeb015d2ac28396ea216a2eae5ae72de72143')
install=wails.install

prepare() {
  mkdir -vp $pkgname-$pkgver/build
}

build() {
  cd $pkgname-$pkgver/v3
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build -o build/wails ./cmd/wails3
}

#check() {
#  cd $pkgname-$pkgver/v3
#  go test ./...
#}

package() {
  install -vDm 755 $pkgname-$pkgver/v3/build/wails -t "$pkgdir/usr/bin/"
  install -vDm 644 $pkgname-$pkgver/{CHANGELOG,CONTRIBUTORS,README}.md -t "$pkgdir/usr/share/doc/$pkgname/"
  install -vDm 644 $pkgname-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
