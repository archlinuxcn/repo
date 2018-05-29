# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=6.784
pkgrel=1
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
options=('!strip' '!emptydirs')
depends=(
  'pacman>=5.1'
  'sudo'
  'git'
)
makedepends=(
  'go'
)
conflicts=('yay-bin' 'yay-git')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha1sums=('f4783b16fd917894c031856bf5cba372de6c3959')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" install
}
