# Maintainer: KroshKobel <kroshkobel AT gmail DOT com>
# Contributor: graysky <graysky AT archlinux DOT us>
# Contributor: Sebastian Wolf <fatmike30 AT gmail DOT com>
# Contributor: jambus <jambus85 AT yahoo DOT de>
# Contributor: TheWretched <rkaprowski AT gmail DOT com>

pkgname=sharpfonts
pkgver=1
pkgrel=10
pkgdesc="Display sharp and clear fonts on Linux like on Windows XP"
url="http://support.mcsnet.ca/${pkgname}/"
license=("unknown")
depends=('ttf-ms-fonts' 'fontconfig' 'freetype2')
install="sharpfonts.install"
source=(http://support.mcsnet.ca/${pkgname}/sf-upd.tar.bz2 sharpfonts.install sharpfonts.sh)
md5sums=('809c83cd576d452d09d07a662237c07d' '1347de3be491d2576c5567265dbbdfc7' 'af6b1217eedc2cb9ada60dd44d10c8cc')
arch=('any')

package() {
	mkdir -p $pkgdir/etc/fonts/conf.avail/${pkgname}
	mkdir -p $pkgdir/etc/fonts/conf.d

	cp *.conf $pkgdir/etc/fonts/conf.avail/${pkgname}/
	
	install -Dm744 sharpfonts.sh $pkgdir/etc/profile.d/sharpfonts.sh

	cd $pkgdir/etc/fonts/conf.d
	ln -s ../conf.avail/${pkgname}/* .
}
