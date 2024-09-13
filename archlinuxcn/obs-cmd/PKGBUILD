# Maintainer: Sean Snell <ssnell@lakecs.net>

pkgname=obs-cmd
pkgver=0.17.8
pkgrel=1
pkgdesc="A minimal OBS CLI for obs-websocket v5"
arch=('x86_64')
url="https://github.com/grigio/obs-cmd"
license=('MIT')
makedepends=('git' 'rust')
provides=('obs-cmd')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/grigio/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")

# Upstream tar.gz

sha512sums=('b6f9fd0916a8b8deebd775260b30b238fe0c9cc5690b5d46bcb3ce819bd8e9eee3213fdc58ef30cf9e8326e85d54e1e2aad159f7141229adf125462caae3957e')

build() {
  cd "${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  install -Dm 755 "${srcdir}/${pkgname}-${pkgver}/target/release/obs-cmd" "${pkgdir}/usr/bin/obs-cmd"
  install -Dm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname"
}
