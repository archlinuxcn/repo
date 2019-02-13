# Maintainer: Alad Wenter <alad@archlinux.org>
pkgname=aurutils
pkgver=2.2.1
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
        "$pkgname-$pkgver.tar.gz.asc::$url/releases/download/$pkgver/$pkgver.tar.gz.asc")
install=$pkgname.install
depends=('git' 'jq' 'expac' 'diffstat' 'pacutils' 'parallel' 'wget')
optdepends=('bash-completion: bash completion'
            'devtools: aur-chroot'
            'vifm: build file interaction'
            'xdelta3: generate delta files')
sha256sums=('253795fef90bb00fa927d0472c4926bf87090ed089b7d77ff0568f166c738b60'
            'SKIP')
validpgpkeys=('DBE7D3DD8C81D58D0A13D0E76BC26A17B9B7018A') # Alad Wenter <alad@archlinux.org>

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
