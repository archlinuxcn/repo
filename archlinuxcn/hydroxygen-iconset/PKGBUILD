# Maintainer: Alireza Savand <alireza.savand@gmail.com>
# Contributors:
#     * Devin Cofer <ranguvar{AT]archlinux[DOT}us>
#     * William Díaz <wdiaz [at] archlinux [dot] us>
#     * Simone Pignatti <simo91.linux@gmail.com>

pkgname=hydroxygen-iconset
pkgver=20090119
pkgrel=2.1
pkgdesc="GTK+ port of the KDE4 Oxygen icon theme"
arch=('i686' 'x86_64')
url="http://deviantdark.deviantart.com/art/hydroxygen-iconset-100826865"
license=("custom:cc-gnu_gpl")

makedepends=('findutils')
depends=('gtk2')

source=("http://fc04.deviantart.com/fs40/f/2009/019/8/7/hydroxygen_iconset_by_deviantdark.zip"
        'hydroxygen-chtype')
sha256sums=('ff6e22c842c4f8a3f9a38dc6d0f78cfde116e22d8bee606db072b0c03d4389e5'
            'd99f13f554b9b87f2c618247af4413a9276e658e77ebc242bc2b1fbcaaaca4de')
install="$pkgname.install"

package() {
	cd "$srcdir/iconset"

	tar xf hydroxygen_iconset.tar.bz2
	find hydroxygen -type d -print0 | xargs -0 chmod 0775
	find hydroxygen -type f -print0 | xargs -0 chmod 0664
	install -Dm755 "$srcdir/hydroxygen-chtype" "$pkgdir/usr/bin/hydroxygen-chtype"

	install -Dm644 "hydroxygen/COPYING" "$pkgdir/usr/share/licenses/$pkgname/COPYING"
	mkdir -p "$pkgdir/usr/share/icons/"
	mv hydroxygen/ "$pkgdir/usr/share/icons/"
}
