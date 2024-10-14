# Maintainer: Sean Snell <ssnell@lakecs.net>

pkgname=obs-cmd
pkgver=0.17.9
pkgrel=1
pkgdesc="A minimal OBS CLI for obs-websocket v5"
arch=('x86_64')
url="https://github.com/grigio/obs-cmd"
license=('MIT')
makedepends=('git' 'rust')
provides=('obs-cmd')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/grigio/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")

# Upstream tar.gz

sha512sums=('f794db7a578fae66997d9ba79ef0e1450d19e63033554329077fd1c3dd21fd6269b5b8724d93f38da10f856563702cc08c7aa8daab55ef11abb47a4fffdfe4a2')

build() {
  cd "${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  install -Dm 755 "${srcdir}/${pkgname}-${pkgver}/target/release/obs-cmd" "${pkgdir}/usr/bin/obs-cmd"
  install -Dm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
