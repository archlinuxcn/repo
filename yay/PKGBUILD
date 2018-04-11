# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=5.675
pkgrel=1
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
options=('!strip' '!emptydirs')
depends=(
  'sudo'
)
makedepends=(
  'git'
  'go'
)
conflicts=('yay-bin' 'yay-git')
source=("https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha1sums=('b31326cd033a3d10a45e9e58826548d5ddd302ee')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" install
}
