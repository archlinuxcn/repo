# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=9.4.7
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
sha256sums=('ac42db3d31852d28c847785b7ac10b0934ffb746f19db99a03e67450d6c37e5e')

build() {
  export GOPATH="$srcdir"/gopath
  cd "$srcdir/$pkgname-$pkgver"
  EXTRA_GOFLAGS="-modcacherw -trimpath" \
    LDFLAGS="-linkmode external -extldflags \"${LDFLAGS}\"" \
    make VERSION=$pkgver DESTDIR="$pkgdir" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX=/usr install
}
