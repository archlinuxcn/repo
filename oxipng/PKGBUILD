# Maintainer: Nicolas F. <aur@fratti.ch>
pkgname=oxipng
pkgver=2.1.4
pkgrel=1
pkgdesc="A lossless PNG compression optimiser"
arch=('x86_64' 'i686' 'armv7h' 'armv6h' 'arm' 'aarch64')
url="https://github.com/shssoichiro/oxipng"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'rust')
source=("$pkgname-$pkgver.tar.gz::https://github.com/shssoichiro/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('157d8039a3e0cbc29824888c3b9c2651789a4a9dd4c203c735150d3deeba266d')

build() {
  cd "$pkgname-$pkgver"

  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"

  install -Dm755 target/release/oxipng "$pkgdir/usr/bin/oxipng"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
