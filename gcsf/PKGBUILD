# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=gcsf
pkgver=0.1.15
pkgrel=1
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

sha256sums=('012156d0fc980346f23dd15f8664066fb522e93b261e2b0de119d7eb04b9951e'
            '379c996c9cf50bfffdd381d1f9f99695b1af5bab17b0ccd14006999d6e0351c1')

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
