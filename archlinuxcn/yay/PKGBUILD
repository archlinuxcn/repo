# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=10.0.2
pkgrel=1
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
depends=(
  'libalpm.so>=12'
  'sudo'
  'git'
)
makedepends=(
  'go'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha256sums=('18851fefe64d0ae907851dcad9ff9d32183fb380c806fd8f0e6dd3518390e3a4')

build() {
  export GOPATH="$srcdir"/gopath
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"

  cd "$srcdir/$pkgname-$pkgver"
  LDFLAGS="-extldflags \"${LDFLAGS}\"" \
    make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" install
}
