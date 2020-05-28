# Maintainer: Jonathan Duck <duckbrain30@gmail.com>

# Expiremental System electron package, set ELECTRON env to electron
pkgname=typora
pkgver=0.9.89
pkgrel=1
pkgdesc="Typora will give you a seamless experience as both a reader and a writer."
arch=('x86_64')
filename="${pkgname}_${pkgver}_amd64.deb"
license=('custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."')
url="https://typora.io/"
depends=('libxss')
optdepends=(
	'noto-fonts-emoji: Or some other emoji font to see emojis'
	'pandoc: Import/export for extra file formats')
source=("https://typora.io/linux/$filename")
sha512sums=('514e38b3d541a1c4a9d0e20c144e3c8d29c057400a69a65b5948bb306bcd8a4cfe15e880779e22c5fb842c5deae87de4ecd7c691bbd17d7207804d32688555a2')

if [[ ! -z $ELECTRON ]]; then
	depends+=($ELECTRON)
	source+=(typora.js)
	sha512sums+=('8ce47de8b0d0ab4b0323ee4c19a4daaf313513700d8c191faab299bfa21aaba9b55cbcf945914103e5f53607228fec3411a83aea8007b192616ad845a3af5c98')
fi

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	rm -rf "$pkgdir/usr/share/lintian/"
	chmod 4755 "$pkgdir/usr/share/typora/chrome-sandbox"
	sed -i '/Change Log/d' "$pkgdir/usr/share/applications/typora.desktop"
	find "$pkgdir" -type d -exec chmod 755 {} \;
	if [[ ! -z $ELECTRON ]]; then
		appdir="${pkgdir}/usr/share/typora"
		mv "${appdir}" tmp/
		mv tmp/resources/app "${appdir}"
		rm -rf tmp/
		install -Dm755 "typora.js" "${pkgdir}/usr/bin/typora"
	fi
}
