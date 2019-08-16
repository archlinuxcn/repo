# Maintainer : Chris Sakalis <chrissakalis@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: James Rayner <james@archlinux.org>
# Contributor: Partha Chowdhury <kira.laucas@gmail.com>

pkgname=conky-nvidia
_pkgname=conky
pkgver=1.11.5
pkgrel=1
pkgdesc='Lightweight system monitor for X'
provides=('conky')
conflicts=('conky')
url='http://conky.sourceforge.net/'
license=('BSD' 'GPL')
arch=('i686' 'x86_64')
makedepends=('cmake' 'docbook2x' 'docbook-xml' 'man-db' 'perl-xml-libxml' 'perl-xml-sax-expat' 'docbook-xsl' 'git')
depends=('glib2' 'curl' 'lua' 'wireless_tools' 'libxml2' 'libxft' 'libxdamage' 'libxinerama' 'imlib2' 'libxnvctrl' 'libpulse')
source=("https://github.com/brndnmtthws/conky/archive/v${pkgver}.tar.gz")

md5sums=('5eb277341701e9e8128e315998796e86')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"

	cmake \
		-D CMAKE_BUILD_TYPE=Release \
		-D MAINTAINER_MODE=ON \
		-D BUILD_CURL=ON \
		-D BUILD_IMLIB2=ON \
		-D BUILD_JOURNAL=ON \
		-D BUILD_NVIDIA=ON \
		-D BUILD_PULSEAUDIO=ON \
		-D BUILD_RSS=ON \
		-D BUILD_WEATHER_METAR=ON \
		-D BUILD_WEATHER_XOAP=ON \
		-D BUILD_WLAN=ON \
		-D BUILD_XDBE=ON \
		-D BUILD_XSHAPE=ON \
		-D CMAKE_INSTALL_PREFIX=/usr \
		.

	make
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
	install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
	install -Dm644 extras/vim/syntax/conkyrc.vim "${pkgdir}"/usr/share/vim/vimfiles/syntax/conkyrc.vim
	install -Dm644 extras/vim/ftdetect/conkyrc.vim "${pkgdir}"/usr/share/vim/vimfiles/ftdetect/conkyrc.vim
}
