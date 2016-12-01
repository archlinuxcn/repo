# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>
# Previous Maintainer: Denis Meiswinkel <denis.meiswinkel@gmail.com>
# Contributor: Balló György <ballogyor+arch@gmail.com>

pkgname=dee
pkgver=1.2.7
pkgrel=9
pkgdesc="Model to synchronize multiple instances over DBus."
arch=("i686" "x86_64")
url="https://launchpad.net/dee"
license=("LGPL")
depends=("glib2" "icu")
makedepends=("gobject-introspection" "python2" "vala")
source=("https://launchpad.net/${pkgname}/1.0/${pkgver}/+download/${pkgname}-${pkgver}.tar.gz"
        "https://launchpadlibrarian.net/258481465/fix-misleading-indentation.patch")
sha256sums=('1bf0336ce684aa0f48d6eae2469628c1a9b43695a77443bc31a5790aa673bf8a'
            '3bf75bd632d6be88632c0f6113aac5ac5d65e1a01b408c27ea1fd7bb718d6ebd')

prepare() {
  cd $srcdir
  patch -p1 -i $srcdir/fix-misleading-indentation.patch
}

build() {
	cd ${pkgname}-${pkgver}
	export PYTHON="/usr/bin/python2"
	./configure --prefix="/usr" --sysconfdir="/etc" --localstatedir="/var" --disable-{static,tests}
	make
}

package() {
	cd $pkgname-$pkgver
	make DESTDIR="${pkgdir}" install

# Is this useful? Fedora does not include these.
#  # Install GI overrides for python 3 as well
#  install -dm 755 "${pkgdir}"/usr/lib/python3.3/site-packages/gi/overrides
#  ln -s ../../../../python2.7/site-packages/gi/overrides/Dee.py "$pkgdir/usr/lib/python3.3/site-packages/gi/overrides/Dee.py"
}

# vim: ts=2 sw=2 et:
