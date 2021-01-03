# Maintainer: Kevin Song <kevin dot s05 at gmail dot com>

pkgname='starship'
pkgdesc='The cross-shell prompt for astronauts'
pkgver='0.48.0'
pkgrel=1
arch=('x86_64')
url='https://starship.rs/'
license=('ISC')
depends=('zlib' 'openssl' 'gcc-libs')
optdepends=('powerline-fonts: powerline symbols for terminals'
            'noto-fonts-emoji: emoji support for terminals')
makedepends=('rust' 'gcc')
checkdepends=('rust' 'git' 'python')
provides=(starship)
#install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::https://github.com/starship/starship/archive/v${pkgver}.tar.gz")
sha256sums=('23e729ace48ec0bf6d8eff5f99003351463841f3b28fe453faceb62e6f99bae6')

build() {
    cd "$pkgname-$pkgver"
    RUSTUP_TOOLCHAIN=${RUSTUP_TOOLCHAIN:-stable} cargo build --release --locked
}

check() {
    cd "$pkgname-$pkgver"
    RUSTUP_TOOLCHAIN=${RUSTUP_TOOLCHAIN:-stable} cargo test --locked
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "target/release/starship" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
