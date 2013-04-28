# Maintainer: evr <evanroman @ gmail>
# Maintainer: Simon Legner <Simon.Legner@gmail.com>

pkgname=tpfan-admin
pkgver=0.95
pkgrel=7
pkgdesc="GTK+ frontend to monitor system temperature and adjust fan trigger temperatures."
arch=('any')
url="http://www.gambitchess.org/mediawiki/index.php/ThinkPad_Fan_Control"
license=('GPL3')
depends=(tpfand python2-rsvg)
source=(http://launchpad.net/tp-fan/tpfan-admin/$pkgver/+download/tpfan-admin-$pkgver.tar.gz)
md5sums=('8006f5ff4f73c7b1d982f17f4a7debd0')

package() {
	cd "$srcdir/$pkgname-$pkgver"

	sed -i 's|#! /usr/bin/env python|#! /usr/bin/env python2|' src/tpfanadmin/* wrappers/tpfan-admin

	install -d "$pkgdir"/usr/lib/python2.7/site-packages/tpfanadmin
	install -m644 src/tpfanadmin/* "$pkgdir"/usr/lib/python2.7/site-packages/tpfanadmin
	install -d "$pkgdir"/usr/share/tpfan-admin/
	install -m644 share/* "$pkgdir"/usr/share/tpfan-admin/
	install -d "$pkgdir"/usr/bin
	install wrappers/tpfan-admin "$pkgdir"/usr/bin/
	install -d "$pkgdir"/usr/share/tpfan-admin/locales/po
	install -m644 po/* "$pkgdir"/usr/share/tpfan-admin/locales/po
	install -d "$pkgdir"/usr/share/applications
	install -m644 share/tpfan-admin.desktop "$pkgdir"/usr/share/applications
}

