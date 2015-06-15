# Maintainer: tailinchu <use_my_id at gmail dot com>
# Contributor: lspci <agm2819 at gmail dot com>
# Contributor: TuxSpirit <tuxspirit AT archlinux DOT fr>

pkgname=rar
pkgver=5.2.1
pkgrel=1
pkgdesc="A command-line port of the rar compression utility"
arch=('i686' 'x86_64')
url="http://www.rarlab.com"
license=('custom')
depends=('gcc-libs')
backup=('etc/rarfiles.lst')

source_i686=(http://www.rarlab.com/rar/rarlinux-$pkgver.tar.gz)
source_x86_64=(http://www.rarlab.com/rar/rarlinux-x64-$pkgver.tar.gz)

md5sums_i686=('d5a541a74f63b2c712ae6e6cd1d5f50c')
md5sums_x86_64=('7c7139c4405f3277eaad1341f9bf4f8d')

package() {
	cd "$srcdir/rar"
	install -Dm755 rar "$pkgdir/usr/bin/rar"
	install -Dm755 rar_static "$pkgdir/usr/bin/rar_static"
	install -Dm755 default.sfx "$pkgdir/usr/lib/default.sfx"
	install -Dm644 rarfiles.lst "$pkgdir/etc/rarfiles.lst"
	install -Dm644 license.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
