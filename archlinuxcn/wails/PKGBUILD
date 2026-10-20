# Maintainer: w0rty <mawo97 at gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>

pkgname=wails
pkgver=2.17.0 # renovate: datasource=github-tags depName=wailsapp/wails
pkgrel=1
pkgdesc="Create desktop apps using Go and Web Technologies"
arch=(x86_64)
url="https://github.com/wailsapp/wails"
license=(MIT)
depends=('glibc' 'npm' 'gtk3')
makedepends=('go')
optdepends=('docker')
source=($url/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('39bbcde34c693f9594cf5265b502b3a99e2667a55acae51c1e821a5fd02ab3d3704a44f4c57f5928d48c7b03e1487632985383fc2c22f28a5a09172812d93e17')
b2sums=('77cec26f256736914471bf50042f32b9d1ad47ba4ad5be61c3e62cfd51aaf18d799fac6e4e775003612547170a1e4bfb990fab81f3e3f6b2ba4d86123f71e13e')
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
