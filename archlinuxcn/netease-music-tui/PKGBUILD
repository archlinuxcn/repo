# Maintainer: yjun <jerrysteve1101 at gmail dot com>

pkgname=netease-music-tui
pkgver=0.1.4
pkgrel=1
pkgdesc="Netease cloud music terminal client by rust"
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h' 'arm')
url="https://github.com/betta-cyber/netease-music-tui"
license=('MIT')
# dbus is required for mpris to work
depends=('dbus'
         'alsa-lib'
         'openssl')
makedepends=('rust')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/betta-cyber/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('7c7ecd4b7a56365e512a9b209173039d5a9231a306f979ed85d7a616b1fbb3db')

build() {
  cd ${pkgname}-${pkgver}

  # cargo build --release --locked --all-features --target-dir=target
  cargo build --release --all-features --target-dir=target
}

package() {
  cd ${pkgname}-${pkgver}
  
  install -Dm755 target/release/ncmt -t ${pkgdir}/usr/bin/
  install -Dm644 LICENSE -t ${pkgdir}/usr/share/licenses/${pkgname}/
}

# vim: set sw=2 ts=2 et:
