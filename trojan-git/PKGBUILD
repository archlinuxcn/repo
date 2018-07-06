# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=trojan-git
pkgver=r202.ceeba96
pkgrel=1
pkgdesc="An unidentifiable mechanism that helps you bypass GFW"
arch=('x86_64')
url="https://github.com/trojan-gfw/trojan"
license=('GPL3')
depends=('boost-libs' 'openssl')
makedepends=('git' 'cmake' 'boost')
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
    install -Dm644 LICENSE $pkgdir/usr/share/license/$pkgname/LICENSE
    cd $pkgname
    make DESTDIR=$pkgdir install
}
# vim set: ts=4 sw=4 et
