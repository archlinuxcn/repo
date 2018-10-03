# Maintainer: Jonathan Duck <duckbrain30@gmail.com>
pkgname=typora
pkgver=0.9.58
pkgrel=2
pkgdesc="Typora will give you a seamless experience as both a reader and a writer."
arch=('x86_64')
license=('custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."')
url="https://typora.io/"
depends=('gconf' 'libxss' 'electron')
optdepends=('noto-fonts-emoji: Or some other emoji font to see emojis')
source=(
	'typora.js'
	"https://typora.io/./linux/${pkgname}_${pkgver}_amd64.deb"
)
md5sums=('1db6a439117322a7ed4bdcf21fa25530'
         '23e55a05ead4115b415c77c1709aa9e6')

package() {
	_src="$srcdir/$pkgname"
	mkdir -p "$_src"
	bsdtar -xf data.tar.xz -C "$_src/"

	sed -i '/Change Log/d' "$_src/usr/share/applications/typora.desktop"

	install -Dm644 "$_src/usr/share/applications/typora.desktop" "$pkgdir/usr/share/applications/typora.desktop"
	install -Dm644 "$_src/usr/share/doc/typora/copyright" "$pkgdir/usr/share/doc/typora/copyright"
	install -Dm755 "$srcdir/typora.js" "$pkgdir/usr/bin/typora"

	cp -r "$_src/usr/share/icons" "$pkgdir/usr/share/icons"
	cp -r "$_src/usr/share/typora/resources/app" "$pkgdir/usr/share/typora"
}
