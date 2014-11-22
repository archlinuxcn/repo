# Maintainer: Alastair Stuart <alastair@muto.so>

pkgname=ubuntu-font-family-console
pkgver=0.80
pkgrel=0
pkgdesc="Ubuntu font family (console fonts)"
arch=('any')
url="http://font.ubuntu.com/"
license=('custom:Ubuntu Font Licence 1.0')
source=(http://mirrors.us.kernel.org/ubuntu/pool/main/u/ubuntu-font-family-sources/fonts-ubuntu-font-family-console_0.80-0ubuntu2_all.deb
	https://bazaar.launchpad.net/~ufl-contributors/ubuntu-font-licence/trunk/download/head:/ubuntufontlicence1.0-20100927174953-087b4le0svr9mh63-1/ubuntu-font-licence-1.0.txt)
md5sums=('1d4dd9eb0c076612ccfbf85f415be53b'
	 '325a1a9029112a2405e743c7f816427b')

package() {
	tar -xzvf data.tar.gz
	cd "${srcdir}/"
	cd ./usr/share/consolefonts
	install -m755 -d "${pkgdir}/usr/share/consolefonts/"
	install -m644 UbuntuMono-*.psf "${pkgdir}/usr/share/consolefonts/"
	cd "${srcdir}/"
	install -D -m644 ubuntu-font-licence-1.0.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENCE"
}
