# Maintainer: Alad Wenter <alad@archlinux.org>
# Co-Maintainer: Cedric Girard <cgirard.archlinux@valinor.fr>
# Co-Maintainer: Maxim Baz <archlinux@maximbaz.com>
pkgname=aurutils
pkgver=2.3.5
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
#         "$pkgname-$pkgver.tar.gz.asc::$url/releases/download/$pkgver/$pkgver.tar.gz.asc")
install=$pkgname.install
depends=('git' 'jq' 'expac' 'diffstat' 'pacutils' 'wget')
optdepends=('bash-completion: bash completion'
            'devtools: aur-chroot'
            'vifm: build file interaction')
sha256sums=('13c6909c7e44c0619b0fab393c2f62d4f453c595bbd65f5a99077c3344a7bc99')
#             'SKIP')
# validpgpkeys=('DBE7D3DD8C81D58D0A13D0E76BC26A17B9B7018A') # Alad Wenter <alad@archlinux.org>

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
