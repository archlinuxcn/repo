# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=10.0.0
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
sha256sums=('58623457318bb726ee349c87a58c661eb1b91f265f0280391cd5fe3a0f40a215')

build() {
  export GOPATH="$srcdir"/gopath
  cd "$srcdir/$pkgname-$pkgver"
  EXTRA_GOFLAGS="-modcacherw -trimpath" \
    LDFLAGS="-linkmode external -extldflags \"${LDFLAGS}\"" \
    make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX="/usr" install
}
