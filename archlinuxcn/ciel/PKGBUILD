# Maintainer: Kaiyang Wu <origincode@aosc.io>
# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
pkgname=ciel
_pkgname=${pkgname}-rs
pkgver=3.9.8
pkgrel=1
pkgdesc="A tool for controlling multi-layer file systems and containers."
arch=('i686' 'x86_64' 'aarch64')
url="https://github.com/AOSC-Dev/ciel-rs"
license=('MIT')
depends=('systemd' 'dbus' 'openssl' 'libssh2' 'libgit2' 'xz' 'squashfs-tools' 'glibc' 'systemd-libs' 'zlib' 'gcc-libs' 'bash')
makedepends=('rust' 'make' 'gcc')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/AOSC-Dev/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('0c244d9c32fabcddece78b7d02af9203415ff540fb5b425b0a0f935f82eb2001')

prepare() {
    cd ${_pkgname}-${pkgver}

    find . -type f -exec sed -i "s|libexec|lib/$pkgname|g" {} +

    export RUSTUP_TOOLCHAIN=stable
    cargo update
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd ${_pkgname}-${pkgver}
    export LIBSSH2_SYS_USE_PKG_CONFIG=1
    CFLAGS+=' -ffat-lto-objects'
    cargo build --release --frozen --all-features --target-dir=target
}

check() {
    cd ${_pkgname}-${pkgver}
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    cd ${_pkgname}-${pkgver}
    install -Dm755 target/release/${_pkgname} -t "${pkgdir}/usr/bin"

    # Rename the binary
    mv "${pkgdir}/usr/bin/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}"

    # Install assets
    PREFIX="${pkgdir}/usr/" ./install-assets.sh

    # Install the license
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
