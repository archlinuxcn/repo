# Maintainer: Jguer <joaogg3@gmail.com>
pkgname=yay
pkgver=6.727
pkgrel=2
pkgdesc="Yet another yogurt. Pacman wrapper and AUR helper written in go."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/Jguer/yay"
license=('GPL')
options=('!strip' '!emptydirs')
depends=(
  'sudo'
  'git'
)
makedepends=(
  'go'
)
conflicts=('yay-bin' 'yay-git')
source=("https://github.com/Jguer/yay/archive/v${pkgver}.tar.gz")
sha1sums=('31c7320909d378d822035168135e3404c168abc4')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make VERSION=$pkgver DESTDIR="$pkgdir" install
}
