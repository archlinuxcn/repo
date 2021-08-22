# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor: DaZ <daz.root+arch@gmail.com>

pkgname=gnvim
url="https://github.com/vhakulinen/gnvim"
pkgdesc="GUI for neovim, without any web bloat"
pkgver=0.1.6
pkgrel=1
arch=('x86_64')
license=('MIT')
depends=('neovim' 'gtk3' 'webkit2gtk')
makedepends=('cargo' 'rust' 'git')
source=("gnvim-${pkgver}::git+https://github.com/vhakulinen/gnvim.git#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
    cd "$srcdir/${pkgname}-${pkgver}"
    sed -i s';/usr/local/share/gnvim/runtime;/usr/share/gnvim/runtime;' src/main.rs
}

build() {
    cd "$srcdir/${pkgname}-${pkgver}"
    cargo build --release --locked
}

check() {
    cd "$srcdir/${pkgname}-${pkgver}"
    cargo test --release --locked
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    make PREFIX="/usr" DESTDIR="$pkgdir/" install
}
