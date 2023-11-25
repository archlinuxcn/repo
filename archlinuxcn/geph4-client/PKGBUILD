# Maintainer: Dct Mei <dctxmei at yandex dot com>
# Co-Maintainer: RogueGirl <3a33oxx40 at mozmail dot com>

pkgname=geph4-client
pkgver=4.10.1
pkgrel=1
pkgdesc="The command-line Geph client"
arch=('x86_64')
url="https://github.com/geph-official/geph4-client"
license=('GPL3')
depends=('gcc-libs' 'glibc')
makedepends=('cargo')
backup=('etc/default/geph4-client')
options=('!lto')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "geph4-client.default"
        "geph4-client.service")
sha256sums=('ab464320196fdb57eee8e105cdb9a60b8769d06db92eb4f496cf3277e669caeb'
            '4e6ac4d3e31d7bf0fd4cb4b9269bbb124501a07a4701ce9728e857751773e4dd'
            'e3d7e3afb1b524e93e60a80a21773a16de17643865bdf6a1a1f2e17fc2cc8e2d')

prepare() {
    cd "${pkgname}-${pkgver}"
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
    cd "${pkgname}-${pkgver}"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release
}

package() {
    cd "${pkgname}-${pkgver}"
    install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
    install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 "${srcdir}/geph4-client.default" "${pkgdir}/etc/default/geph4-client"
    install -Dm644 "${srcdir}/geph4-client.service" -t "${pkgdir}/usr/lib/systemd/system/"
}
