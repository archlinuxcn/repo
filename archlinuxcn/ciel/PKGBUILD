# Maintainer: Kaiyang Wu <origincode@aosc.io>
pkgname=ciel
_pkgname=${pkgname}-rs
pkgver=3.1.2
pkgrel=2
pkgdesc="A tool for controlling multi-layer file systems and containers."
arch=('i686' 'x86_64')
url="https://github.com/AOSC-Dev/ciel-rs"
license=('MIT')
depends=('systemd' 'dbus' 'openssl' 'libssh2' 'libgit2' 'xz')
makedepends=('rust' 'make' 'gcc')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/AOSC-Dev/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('7e3bd494b7e137b7a531dea3d7cd5d4eda0d7a48a82f48615d4d1e8985fad523')
conflicts=('ciel-git')

build() {
    cd ${_pkgname}-${pkgver}
    LIBSSH2_SYS_USE_PKG_CONFIG=1 cargo build --release --locked --all-features --target-dir=target
}

package() {
    cd ${_pkgname}-${pkgver}
    install -Dm755 target/release/${_pkgname} -t "${pkgdir}/usr/bin"

    # Rename the binary
    mv -v "${pkgdir}/usr/bin/ciel-rs" "${pkgdir}/usr/bin/ciel"

    # Install assets
    PREFIX="${pkgdir}/usr/" ./install-assets.sh

    # Install the license
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
