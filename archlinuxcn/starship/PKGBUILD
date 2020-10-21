# Maintainer: Kevin Song <kevin dot s05 at gmail dot com>

pkgname='starship'
pkgdesc='The cross-shell prompt for astronauts'
pkgver=0.46.2
pkgrel=1
arch=('x86_64')
url='https://starship.rs/'
license=('ISC')
depends=('zlib' 'gcc-libs' 'openssl')
optdepends=('powerline-fonts: powerline symbols for terminals'
            'noto-fonts-emoji: emoji support for terminals')
makedepends=('rust' 'gcc')
checkdepends=('rust' 'git' 'python')
provides=(starship)
#install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::https://github.com/starship/starship/archive/v${pkgver}.tar.gz")
sha256sums=('39301c8118239eda7b6d8dbcae498f28bfd901932e69003c249d99ee7989c1bb')

build() {
    cd "$pkgname-$pkgver"
    cargo build --release --locked
}

check() {
    cd "$pkgname-$pkgver"
    cargo test --locked
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "target/release/starship" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
