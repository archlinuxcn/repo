# Maintainer: Alad Wenter <alad@archlinux.org>
# Co-Maintainer: Cedric Girard <cgirard.archlinux@valinor.fr>
# Co-Maintainer: Maxim Baz <archlinux@maximbaz.com>
pkgname=aurutils
pkgver=2.3.6b
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
sha256sums=('22b12a7161635622f86cb4c4dd28c79ae9e6c23e60f3ef7985d107879c64d004')
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
