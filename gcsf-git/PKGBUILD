# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=gcsf-git
pkgver=r186.38ef33b
pkgrel=1
pkgdesc="a FUSE file system based on Google Drive (Written by Rust)"
arch=('x86_64')
depends=('fuse2' 'gcc-libs')
makedepends=('git' 'rust')
optdepends=("ranger: A simple, vim-like file manager")
conflicts=("gcsf")
provides=("gcsf")
url="https://github.com/harababurel/gcsf"
license=('MIT')
install="gcsf-git.install"

source=("$pkgname::git+$url.git"
		"gcsf-git.install")

sha256sums=('SKIP'
            '379c996c9cf50bfffdd381d1f9f99695b1af5bab17b0ccd14006999d6e0351c1')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd $pkgname
    cargo fmt --all -- --check
    cargo build --release
}

package() {
    cd $srcdir/$pkgname

    # License
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    # Binaries
    install -Dm755 target/release/gcsf $pkgdir/usr/bin/gcsf
}
# vim set: ts=4 sw=4 et
