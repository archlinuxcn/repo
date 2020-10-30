# Maintainer: Alad Wenter <https://github.com/AladW>
pkgname=aurutils
pkgver=3.0.0
pkgrel=2
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz"
        "$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz.signify"
        'aurutils.pub')
changelog=aurutils.changelog
sha256sums=('b28da1527b2c6dddbe3aa00f79a0264b54fb671796f1fd9d03cb2f46e9cae8f9'
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
    cd aurutils
    make DESTDIR="$pkgdir"
}

package() {
    cd aurutils
    make DESTDIR="$pkgdir" install
}
