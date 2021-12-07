# Maintainer: Alad Wenter <https://github.com/AladW>
pkgname=aurutils
pkgver=3.2.2
pkgrel=3
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz"
        "aur-view-arg-file.patch::$url/commit/aa2cb0aadbe26bbecd5cc5c1a180f6ddb2edd1ab.patch")
changelog=aurutils.changelog
install=aurutils.install
sha256sums=('6bbc6949d27b1132828aa3e68ad2252d8125365c9b7bec6c587fd15bf3081f72'
            '531048b96cf9217bb3c5f6eebc922a0ebfe262a26ff3f0dcfb5cdb59d66f974c')
depends=('git' 'jq' 'pacutils' 'curl' 'expect')
optdepends=('bash-completion: bash completion'
            'zsh: zsh completion'
            'devtools: aur-chroot'
            'vifm: default pager')

prepare() {
    cd "$pkgname-$pkgver"
    patch -p1 < "$srcdir"/aur-view-arg-file.patch # issue 871
}

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
