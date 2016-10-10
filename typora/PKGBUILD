# Maintainer: Jonathan Duck <duckbrain30@gmail.com>
pkgname=typora
pkgver=0.9.20
pkgrel=1
pkgdesc="Typora will give you a seamless experience as both a reader and a writer."
arch=('x86_64')
filename="${pkgname}_${pkgver}_amd64.deb"
license=('custom:"Copyright (c) 2014 GitHub Inc."')
url="https://typora.io/"
source=("https://typora.io/./linux/$filename")
md5sums=('bfe7b4f0c12b1c5d8d35882407f6ec97')

package() {
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	rm -rf "${pkgdir}"/usr/share/lintian/
	chmod -R 755 "$pkgdir"
}
