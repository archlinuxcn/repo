# Maintainer: Evan Purkhiser <evanpurkhiser@gmail.com>

_gitname=linux-vt-setcolors

pkgname=setcolors-git
pkgver=0.0.0
pkgrel=1
pkgdesc="Allows you to set the linux VT101 default color palette"
arch=('i686' 'x86_64')
license=('MIT')
url="https://github.com/EvanPurkhiser/${_gitname}"
depends=(glibc)
makedepends=(git)
source=("git://github.com/EvanPurkhiser/${_gitname}")
md5sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_gitname}"
	echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
	cd "${srcdir}/${_gitname}"
	make
}

package() {
	cd "${srcdir}/${_gitname}"

	make PREFIX=/usr DESTDIR="${pkgdir}" install
	install -Dm 644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
