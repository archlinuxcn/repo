# Maintainer: Kevin Song <kevin dot s05 at gmail dot com>

pkgname='starship'
pkgdesc='The cross-shell prompt for astronauts'
pkgver=0.47.0
pkgrel=1
arch=('x86_64')
url='https://starship.rs/'
license=('ISC')
depends=('zlib' 'openssl')
optdepends=('powerline-fonts: powerline symbols for terminals'
            'noto-fonts-emoji: emoji support for terminals')
makedepends=('rust' 'gcc')
checkdepends=('rust' 'git' 'python')
provides=(starship)
#install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::https://github.com/starship/starship/archive/v${pkgver}.tar.gz")
sha256sums=('9c9ede1eb7a9e1acf49f0321915232426c234b356c6bb1f740d15d6fa45d1bee')

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
