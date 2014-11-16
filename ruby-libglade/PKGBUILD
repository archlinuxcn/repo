# Contributors:
#	Andrea Scarpino <bash.lnx@gmail.com>
# 	Bjorn Lindeijer <bjorn@lindeijer.nl>
# 	thomas <vidvandre@gmail.com>
#	henning mueller <henning@orgizm.net>

pkgname=ruby-libglade
pkgver=0.90.5
pkgrel=1
pkgdesc='Ruby libglade2 bindings.'
arch=(i686 x86_64)
url='http://ruby-gnome2.sourceforge.jp'
license=(LGPL)
depends=(ruby-gtk2 libglade)
makedepends=(ruby-pkgconfig)
source=(
	http://downloads.sourceforge.net/ruby-gnome2/ruby-gnome2-all-$pkgver.tar.gz
)
md5sums=(
	58ee234ef8b121b11de8a245c61cd4a9
)

build() {
	cd $srcdir/ruby-gnome2-all-$pkgver
	ruby extconf.rb libglade
	make
}

package() {
	cd $srcdir/ruby-gnome2-all-$pkgver
	make DESTDIR=$pkgdir install 
}
