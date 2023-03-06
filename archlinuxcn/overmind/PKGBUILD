#!/hint/bash -e
# Maintainer: Adrien Smith <adrien@panissupraomnia.dev>

pkgname=overmind
pkgver=2.4.0
pkgrel=1
pkgdesc="Process manager for Procfile-based applications and tmux"
arch=("x86_64")
url="https://github.com/DarthSim/$pkgname"
license=("MIT")
depends=('tmux')
makedepends=("go")
conflicts=("$pkgname-bin" "$pkgname-git")
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('6936349e4a2d5fdae97ba35f4e0f92f3e466fd439b217ef3e84cf469e7a18816')
b2sums=('c102283677b39e18152081830df69aa89ff12d27d10be6ce8355ed50cc1eadf22eef7e756f22f8b29a69a447b2633c3ebf834f5634c6b3808f15029644961da6')

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o $pkgname .
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
