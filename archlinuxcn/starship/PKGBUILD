# Maintainer: Kevin Song <kevin dot s05 at gmail dot com>

pkgname='starship'
pkgdesc='The cross-shell prompt for astronauts'
pkgver='0.50.0'
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
sha256sums=('d8f4dc9bd266f2a5c34926d361c62fdddb61cd7da4acadba5f9c175eb07602e5')

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
    targetdir=${CARGO_TARGET_DIR:-target}
    install -Dm755 "$targetdir/release/starship" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
