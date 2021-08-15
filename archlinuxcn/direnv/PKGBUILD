# Maintainer: zimbatm <zimbatm@zimbatm.com>
# Maintainer: ShadowKyogre <shadowkyogre.public+aur@gmail.com>
# Maintainer: rmorgans <rick.morgans@gmail.com>
pkgname=direnv
pkgver=2.28.0
pkgrel=1
pkgdesc='a shell extension that manages your environment'
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url='https://direnv.net'
license=('MIT')
makedepends=('go' 'gcc' 'make')
conflicts=("$pkgname")
provides=("$pkgname")
source=("$pkgname-$pkgver.tar.gz::https://github.com/direnv/direnv/archive/v$pkgver.tar.gz")
sha256sums=('fa539c63034b6161d8238299bb516dcec79e8905cd43ff2b9559ad6bf047cc93')

_gopackagepath=github.com/direnv/direnv

build() {
  cd "$pkgname-$pkgver"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
  go build -o $pkgname
}

check() {
  cd "$pkgname-$pkgver"
  go test -v
  bash ./test/direnv-test.bash
  ./test/stdlib.bash
}

package() {
  cd "$pkgname-$pkgver"
  make install PREFIX=/usr DESTDIR="$pkgdir"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
