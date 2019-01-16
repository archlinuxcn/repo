# Maintainer: Michel Wohlert <michel.wohlert@gmail.com>

pkgname=games_nebula
pkgver=20180605
pkgrel=2
pkgdesc='Unofficial Linux client for GOG'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/yancharkin/games_nebula'
install="${pkgname}.install"
depends=('python-gobject' 'python-beautifulsoup4' 'python-lxml' 'python-pillow' 'python-requests' 'python-pytz' 'webkit2gtk' 'innoextract' 'htmlcxx' 'lgogdownloader' 'xorg-xrandr' 'curl' 'p7zip')
makedepends=()
optdepends=('gksu' 'xterm' 'tar' 'cabextract' 'unshield' 'ffmpeg' 'wine' 'winetricks' 'dosbox' 'scummvm' 'megatools')
provides=('games_nebula')
conflicts=('games_nebula')
source=(${pkgname}_${pkgver}.tar.gz::"https://github.com/yancharkin/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('4803b3e19e2ed7725dc16feeb69a7a96d14a53d521f8c90c154b1dd21ce3902c')

package() {
	mkdir -p "$pkgdir/opt/${pkgname}/"
	cp -dr --no-preserve=ownership "$srcdir/${pkgname}-${pkgver}/." "$pkgdir/opt/${pkgname}/"
        
        install -dm755 "${pkgdir}/usr/bin"
	echo '#!/bin/bash
	python "/opt/games_nebula/games_nebula.py"' > "${pkgdir}/usr/bin/${pkgname}"
	chmod 755 "${pkgdir}/usr/bin/${pkgname}"
	
	install -dm755 "${pkgdir}/usr/share/applications/"
	echo "[Desktop Entry]
	Name=Games Nebula
	Comment=Application for managing and playing games
	Exec=/usr/bin/${pkgname}
	Icon=/opt/${pkgname}/images/icon.png
	Type=Application
	Terminal=false
	Categories=Game;" > "${pkgdir}/usr/share/applications/${pkgname}.desktop"
	chmod 644 "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}

