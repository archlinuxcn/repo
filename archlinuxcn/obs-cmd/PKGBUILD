# Maintainer: Sean Snell <ssnell@lakecs.net>

pkgname=obs-cmd
pkgver=0.18.5
pkgrel=1
pkgdesc="A minimal OBS CLI for obs-websocket v5"
arch=('x86_64')
url="https://github.com/grigio/obs-cmd"
license=('MIT')
makedepends=('git' 'rust')
provides=('obs-cmd')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/grigio/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")

# Upstream tar.gz
sha512sums=('194ce75a9c95701d37df68769086d3c2662926ee023c4936571197b1e221e2c5070916937230d009cd6b198370dd0fb3e21be5caf37bb73796b5a8aa1fa7f1d6')

build() {
  cd "${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  install -Dm 755 "${srcdir}/${pkgname}-${pkgver}/target/release/obs-cmd" "${pkgdir}/usr/bin/obs-cmd"
  install -Dm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
