# Maintainer: Alad Wenter <alad@archlinux.org>
# Co-Maintainer: Cedric Girard <cgirard.archlinux@valinor.fr>
pkgname=aurutils
pkgver=2.3.1
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
        #"$pkgname-$pkgver.tar.gz.asc::$url/releases/download/$pkgver/$pkgver.tar.gz.asc")
install=$pkgname.install
depends=('git' 'jq' 'expac' 'diffstat' 'pacutils' 'parallel' 'wget')
optdepends=('bash-completion: bash completion'
            'devtools: aur-chroot'
            'vifm: build file interaction'
            'xdelta3: generate delta files')
sha256sums=('2e8c7656c620c1c8ded07e20cc9e9cb37d7a4bb234c9f5bd166a2e3887d3db65')
validpgpkeys=('DBE7D3DD8C81D58D0A13D0E76BC26A17B9B7018A') # Alad Wenter <alad@archlinux.org>

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
