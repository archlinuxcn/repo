# Maintainer: Jonas Bögle <aur@iwr.sh>
# Contributor: Jonathan Duck <duckbrain30@gmail.com>

pkgname=typora
pkgver=0.11.14
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
sha512sums=('cd0ea7a906ca85adebec9be473fa8b2e972f4c8932f13831723d7a48c8b64ebc8a823ce5e89c9fff2a94f22103dc65ca14d775a05e1167fb54d9d21dd7afc870')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	rm -rf "$pkgdir/usr/share/lintian/"
	chmod 4755 "$pkgdir/usr/share/typora/chrome-sandbox"
	# Remove write permission for group/other
	chmod -R go-w "$pkgdir/usr/share/typora/resources/node_modules"
	sed -i '/Change Log/d' "$pkgdir/usr/share/applications/typora.desktop"
	find "$pkgdir" -type d -exec chmod 755 {} \;
}
