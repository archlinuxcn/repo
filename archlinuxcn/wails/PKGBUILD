# Maintainer: w0rty <mawo97 at gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>

pkgname=wails
pkgver=2.12.0 # renovate: datasource=github-tags depName=wailsapp/wails
pkgrel=2
pkgdesc="Create desktop apps using Go and Web Technologies"
arch=(x86_64)
url="https://github.com/wailsapp/wails"
license=(MIT)
depends=('glibc' 'npm' 'gtk3')
makedepends=('go')
optdepends=('docker')
source=($url/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('d48cae44069dfd7a0ee73508182bc7e6e595a98e248b150cbec3b5bcfbe86a19fc4b27c0c30520fb1908112ffd23362ddeea24ab036a7643de9e25381e73aea2')
b2sums=('eeee1f5f72e3324d053fb8de7237073efbe830eb35e363d31789c2790a627c59dc55e78468a2977104c70d7c03329e4287fb65b143395fa977612a5cb6b0642c')
install=wails.install

prepare() {
  mkdir -vp $pkgname-$pkgver/build
}

build() {
  cd $pkgname-$pkgver/v2
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build -o build/ ./cmd/wails
}

#check() {
#  cd $pkgname-$pkgver/v2
#  go test ./...
#}

package() {
  install -vDm 755 $pkgname-$pkgver/v2/build/$pkgname -t "$pkgdir/usr/bin/"
  install -vDm 644 $pkgname-$pkgver/{CHANGELOG,CONTRIBUTORS,README}.md -t "$pkgdir/usr/share/doc/$pkgname/"
  install -vDm 644 $pkgname-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
