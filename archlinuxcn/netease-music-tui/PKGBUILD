# Maintainer: yjun <jerrysteve1101 at gmail dot com>

pkgname=netease-music-tui
pkgver=0.1.5
pkgrel=1
pkgdesc="Netease cloud music terminal client by rust"
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h' 'arm')
url="https://github.com/betta-cyber/netease-music-tui"
license=('MIT')
# dbus is required for mpris to work
depends=('dbus'
         'alsa-lib'
         'openssl')
makedepends=('cargo')
source=(${pkgname}-${pkgver}.tar.gz::"https://github.com/betta-cyber/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('52c841da0970b982c0ed316fb5d0c2688123f73ba3dec490bf4fcb2668140956')

prepare() {
  cd ${pkgname}-${pkgver}

  # cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
  cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd ${pkgname}-${pkgver}

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

# check() {
#    export RUSTUP_TOOLCHAIN=stable
#    cargo test --frozen --all-features
# }

package() {
  cd ${pkgname}-${pkgver}
  
  install -Dm755 target/release/ncmt -t ${pkgdir}/usr/bin/
  install -Dm644 LICENSE -t ${pkgdir}/usr/share/licenses/${pkgname}/
}

# vim: set sw=2 ts=2 et:
