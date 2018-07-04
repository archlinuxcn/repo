# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=gcsf
pkgver=0.1.14
pkgrel=2
pkgdesc="a FUSE file system based on Google Drive (Written by Rust)"
arch=('x86_64')
depends=('fuse2' 'gcc-libs' 'pkgconf')
makedepends=('git' 'rust')
optdepends=("ranger: A simple, vim-like file manager")
conflicts=("gcsf")
provides=("gcsf")
url="https://github.com/harababurel/gcsf"
license=('MIT')
install="gcsf.install"

source=("$pkgname.tar.gz::https://github.com/harababurel/gcsf/archive/$pkgver.tar.gz"
        "gcsf.install")

sha256sums=('85edd86696eb4ef58a5cdc9e455298ec5d99edf107a1d8bcaa22acf4cd6d0322'
            '3cd6b36903ea832e855f07b7ec76612a10f03fccfc893fb58b23e4a12b104ab9')

build() {
    cd $pkgname-$pkgver
    cargo fmt --all -- --write-mode=diff
    cargo build --release
}

package() {
    cd $srcdir/$pkgname-$pkgver

    # License
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    # Binaries
    install -Dm755 target/release/gcsf $pkgdir/usr/bin/gcsf
}
# vim set: ts=4 sw=4 et
