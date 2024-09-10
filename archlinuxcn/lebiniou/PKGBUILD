# Maintainer: opale95
# Contributor: yochananmarqos
pkgname=lebiniou
pkgver=3.67.0
pkgrel=2
pkgdesc="User-friendly, powerful music visualization / VJing tool"
arch=('x86_64' 'pentium4' 'i686')
url="https://biniou.lenain.info/"
license=('GPL')
depends=('imagemagick' 'fftw' 'sdl2' 'libcaca' 'ffmpeg' 'lebiniou-data>=3.67.0' 'ulfius')
source=("https://gitlab.com/lebiniou/lebiniou/-/archive/version-$pkgver/lebiniou-version-$pkgver.tar.gz")
sha256sums=('35e2bf5e1675a4faeed7956f45ad1a764e881c76f40d8d3da6cc8ba05c441250')

build() {
	cd "$pkgname-version-$pkgver"
	./bootstrap
	./configure --prefix=/usr
	make
}

package() {
	cd "$pkgname-version-$pkgver"
	make DESTDIR="$pkgdir/" install
}

