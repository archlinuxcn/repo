pkgname=devilspie2
pkgver=0.45
pkgrel=1
pkgdesc="A window matching utility, allowing the user to perform scripted actions on windows as they are created."
arch=('i686' 'x86_64')
url="https://www.nongnu.org/$pkgname/"
license=('GPL-3.0-or-later')
depends=('lua>=5.1' 'gtk3' 'libwnck3')
source=("https://download.savannah.nongnu.org/releases/$pkgname/${pkgname}_$pkgver-src.tar.gz"{,.asc})
sha256sums=('6cc55a68ccfd8bb5620f4cd7c9913ef29aba8a9e96648497c5b448fdb97cb034'
            'SKIP')
validpgpkeys=('A523530DD1E9FDDFAD3D5FCAA9B57A926EF302F5') # Darren Salt <devspam@moreofthesa.me.uk>

build() {
	cd "$pkgname-$pkgver"
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" PREFIX=/usr install

	# Install documentation
	mkdir -p -m755 "$pkgdir/usr/share/doc"
	cp -Rp doc/ "$pkgdir/usr/share/doc/$pkgname"
	install -Dp -m644 README "$pkgdir/usr/share/doc/$pkgname/README"
}

# vim: set ft=sh ts=4 sw=4 noet:
