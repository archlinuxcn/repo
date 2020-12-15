# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=10.1.2
pkgrel=1
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
depends=(
  'pacman>5'
  'sudo'
  'git'
)
makedepends=(
  'go'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha256sums=('203ac178fcece5edbeaae40813b69f49d9af346a9bb4579252ba4a2eb2225f52')

build() {
  export GOPATH="$srcdir"/gopath
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_ENABLED=1

  cd "$srcdir/$pkgname-$pkgver"
  LDFLAGS="-extldflags \"${LDFLAGS}\"" \
    make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" install
}
