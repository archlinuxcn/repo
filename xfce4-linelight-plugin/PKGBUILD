# Maintainer: Spike29 <leguen.yannick@gmail.com>
# Contributor: Michael Pfeuti <m_pfeuti@students.unibe.ch>

pkgname='xfce4-linelight-plugin'
pkgver='0.1.7'
pkgrel='8'
pkgdesc='A simple frontend for the locate search.'
arch=('i686' 'x86_64')
license=('GPL2')
url='http://goodies.xfce.org/projects/panel-plugins/xfce4-linelight-plugin'
groups=('xfce4-goodies')
depends=('xfce4-panel' 'libxfcegui4' 'mlocate')
options=('!libtool')
install="${pkgname}.install"
source=("http://ftp.de.debian.org/debian/pool/main/x/${pkgname}/${pkgname}_${pkgver}.orig.tar.bz2"
	"http://lionel.lefolgoc.net/misc/01_port-to-xfcerc.patch")
md5sums=('1915cd661aafd09c08e04d65775a78ce'
	 '8b04c70513ecbf74412ea3ed230c46a3')

build() {
	cd "$srcdir/"
	patch -p0 -i 01_port-to-xfcerc.patch
	cd "$pkgname-$pkgver/"
	./configure --prefix=/usr --sysconfdir=/etc --libexecdir=/usr/lib/ \
	--localstatedir=/var --disable-static
	make	
}

package() {
	cd "$srcdir/$pkgname-$pkgver/"
	make DESTDIR="$pkgdir" install
}
