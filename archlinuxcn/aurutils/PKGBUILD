# Maintainer: Alad Wenter <https://github.com/AladW>
pkgname=aurutils
pkgver=3.0.3
pkgrel=2
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz"
        "$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz.signify"
        'aurutils.pub')
changelog=aurutils.changelog
sha256sums=('1025530a44d25caccb4e6a1fe0e44474dbdecfd74e7822da78aaa369cff9d06c'
            'SKIP'
            'f11d869b344b01acb229db00fcd40f72a6ee1d3b080b0bc2870001ed94f99dc9')
depends=('git' 'jq' 'pacutils' 'curl')
makedepends=('signify')
optdepends=('bash-completion: bash completion'
            'zsh: zsh completion'
            'devtools: aur-chroot'
            'vifm: default pager')

prepare() {
    signify -V -p aurutils.pub -m "$pkgname-$pkgver".tar.gz \
            -x "$pkgname-$pkgver".tar.gz.signify
}

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
