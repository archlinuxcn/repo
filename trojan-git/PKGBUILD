# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=trojan-git
pkgver=r228.6d66df4
pkgrel=2
pkgdesc="An unidentifiable mechanism that helps you bypass GFW"
arch=('x86_64')
url="https://github.com/trojan-gfw/trojan"
license=('GPL3')
depends=('boost-libs' 'libmariadbclient')
optdepends=('ca-certificates: server certificate verification' 'mariadb: advanced user management')
makedepends=('git' 'cmake' 'boost' 'openssl' 'libmariadbclient')
source=("$pkgname::git+$url"
        "https://raw.githubusercontent.com/trojan-gfw/trojan/master/LICENSE")
backup=('etc/trojan/config.json')
sha512sums=('SKIP'
            '552aec8d120c9d931769f6a6b794716fce978d0055715de21746dc0f064f4a0f72b6be42d4828b98a56715b23fa427c1f66fd20aca0ef1751cc384c420db1605')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd $pkgname
    cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
    make
}

package() {
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
    cd $pkgname
    make DESTDIR=$pkgdir install
}
# vim set: ts=4 sw=4 et
