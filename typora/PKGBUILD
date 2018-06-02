# Maintainer: Jonathan Duck <duckbrain30@gmail.com>
pkgname=typora
pkgver=0.9.53
pkgrel=1
pkgdesc="Typora will give you a seamless experience as both a reader and a writer."
arch=('x86_64')
filename="${pkgname}_${pkgver}_amd64.deb"
license=('custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."')
url="https://typora.io/"
depends=('gconf' 'libxss')
optdepends=('noto-fonts-emoji: Or some other emoji font to see emojis')
source=("https://typora.io/./linux/$filename")
md5sums=('7bf938aa11cc6b8d3dca442e673b057b')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	rm -rf "$pkgdir/usr/share/lintian/"
	sed -i '/Change Log/d' "$pkgdir/usr/share/applications/typora.desktop"
	find "$pkgdir" -type d -exec chmod 755 {} \;
}
