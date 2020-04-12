# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=9.4.6
pkgrel=2
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
depends=(
  'pacman>=5.2'
  'sudo'
  'git'
)
makedepends=(
  'go'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha1sums=('a3b2dd86fda1cc5998899cd69df2102e57ab8fbc')

build() {
  export GOPATH="$srcdir"/gopath
  cd "$srcdir/$pkgname-$pkgver"
  EXTRA_GOFLAGS="-modcacherw -gcflags all=-trimpath=${PWD} -asmflags all=-trimpath=${PWD}" \
    LDFLAGS="-linkmode external -extldflags \"${LDFLAGS}\"" \
    make VERSION=$pkgver DESTDIR="$pkgdir" build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" PREFIX=/usr install
}
