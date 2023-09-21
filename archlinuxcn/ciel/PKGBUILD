# Maintainer: Kaiyang Wu <origincode@aosc.io>
pkgname=ciel
_pkgname=${pkgname}-rs
pkgver=3.2.0
pkgrel=1
pkgdesc="A tool for controlling multi-layer file systems and containers."
arch=('i686' 'x86_64')
url="https://github.com/AOSC-Dev/ciel-rs"
license=('MIT')
depends=('systemd' 'dbus' 'openssl' 'libssh2' 'libgit2' 'xz')
makedepends=('rust' 'make' 'gcc')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/AOSC-Dev/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('c2a631a7822f9cc0ec787c7af4de10d5971abaa04ba9f69b9f4a34d6dda6b529')
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
