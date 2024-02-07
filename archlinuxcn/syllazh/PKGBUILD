# Maintainer: oldherl <oldherl@gmail.com>

pkgname=syllazh
pkgver=0.1
pkgrel=1
pkgdesc="Linux TTY font for Chinese, but treat it as a syllabic writing"
url='https://github.com/oldherl/syllazh/'
arch=('any')
source=($pkgname.tar.gz::https://github.com/oldherl/$pkgname/releases/download/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('SKIP')
license=("OFL-1.1")

package() {
    cd "${srcdir}/$pkgname/"
	find . -name '*.psfu.gz' -execdir install -Dm644 {} $pkgdir/usr/share/kbd/consolefonts/{} \;
	install -D -m644 "${srcdir}/$pkgname/OFL.txt" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
