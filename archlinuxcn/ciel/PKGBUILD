# Maintainer: Jack Wu <origincode@aosc.io>
pkgname=ciel
_pkgname=${pkgname}-rs
pkgver=3.1.0
pkgrel=1
pkgdesc="A tool for controlling multi-layer file systems and containers."
arch=('i686' 'x86_64')
url="https://github.com/AOSC-Dev/ciel-rs"
license=('MIT')
depends=('systemd' 'dbus' 'openssl')
makedepends=('rust' 'make' 'gcc')
optdepends=('libgit2: git vcs support'
            'xz: xzip archive support')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/AOSC-Dev/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('f0dd120a8924ae7bd8743d677addb8a368518d6ae37b6a0553c2411ed6a24d60')
conflicts=('ciel-git')

build() {
    cd ${_pkgname}-${pkgver}
    cargo build --release --locked --all-features --target-dir=target
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
