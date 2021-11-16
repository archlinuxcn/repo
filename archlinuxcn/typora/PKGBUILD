# Maintainer: Jonas Bögle <aur@iwr.sh>
# Contributor: Jonathan Duck <duckbrain30@gmail.com>

pkgname=typora
pkgver=0.11.16
pkgrel=1
pkgdesc="A minimal markdown editor and reader."
arch=('x86_64')
filename="${pkgname}_${pkgver}_amd64.deb"
license=('custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."')
url="https://typora.io/"
depends=('libxss')
optdepends=(
	'noto-fonts-emoji: Or some other emoji font to see emojis'
	'pandoc: Import/export for extra file formats')
source=("https://typora.io/linux/$filename")
sha512sums=('49a3ca0b8b5f6b5639a58cc6d51c4b4ff97325ba8536687a060ef0187b5e720316b11b77748e47f50506f5b7da59076a606bee124302e827893503b60b4e2017')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	rm -rf "$pkgdir/usr/share/lintian/"
	chmod 4755 "$pkgdir/usr/share/typora/chrome-sandbox"
	# Remove write permission for group/other
	chmod -R go-w "$pkgdir/usr/share/typora/resources/node_modules"
	sed -i '/Change Log/d' "$pkgdir/usr/share/applications/typora.desktop"
	find "$pkgdir" -type d -exec chmod 755 {} \;
}
