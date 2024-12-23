# Maintainer: Sean Snell <ssnell@lakecs.net>

pkgname=obs-cmd
pkgver=0.18.0
pkgrel=1
pkgdesc="A minimal OBS CLI for obs-websocket v5"
arch=('x86_64')
url="https://github.com/grigio/obs-cmd"
license=('MIT')
makedepends=('git' 'rust')
provides=('obs-cmd')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/grigio/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")

# Upstream tar.gz
sha512sums=('56497b6a402c0f065765f8d6374913abbe3a7387b0ba0ef48bfb0da98f5830ec4909cd9065ad47c2c521ae2979027d544d5e9c2949ade24fd6d460021a596145')

build() {
  cd "${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  install -Dm 755 "${srcdir}/${pkgname}-${pkgver}/target/release/obs-cmd" "${pkgdir}/usr/bin/obs-cmd"
  install -Dm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
