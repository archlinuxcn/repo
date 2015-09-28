# Maintainer: KroshKobel <kroshkobel AT gmail DOT com>
# Contributor: graysky <graysky AT archlinux DOT us>
# Contributor: Sebastian Wolf <fatmike30 AT gmail DOT com>
# Contributor: jambus <jambus85 AT yahoo DOT de>
# Contributor: TheWretched <rkaprowski AT gmail DOT com>

pkgname=sharpfonts
pkgver=1
pkgrel=8
pkgdesc="Display sharp and clear fonts on Linux like on Windows XP"
url="http://support.mcsnet.ca/${pkgname}/"
license=("unknown")
depends=('ttf-ms-fonts' 'fontconfig' 'freetype2')
install="sharpfonts.install"
source=(http://support.mcsnet.ca/${pkgname}/sf-upd.tar.bz2 sharpfonts.install)
md5sums=('809c83cd576d452d09d07a662237c07d' '1347de3be491d2576c5567265dbbdfc7')
arch=('any')

package() {
	mkdir -p $pkgdir/etc/fonts/conf.avail/${pkgname}
	mkdir -p $pkgdir/etc/fonts/conf.d

	cp *.conf $pkgdir/etc/fonts/conf.avail/${pkgname}/

	cd $pkgdir/etc/fonts/conf.d
	ln -s ../conf.avail/${pkgname}/* .
}
