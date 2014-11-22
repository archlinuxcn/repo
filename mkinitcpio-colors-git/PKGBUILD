# Maintainer: Evan Purkhiser <evanpurkhiser@gmail.com>

_gitname=mkinitcpio-colors

pkgname=mkinitcpio-colors-git
pkgver=0.0.0
pkgrel=1
pkgdesc="mkinitcpio hook to set VT console colors during early userspace"
arch=(any)
license=('MIT')
url="https://github.com/EvanPurkhiser/${_gitname}"
install="usage.install"
depends=(mkinitcpio setcolors-git)
makedepends=(git)
source=("git://github.com/EvanPurkhiser/${_gitname}")
md5sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_gitname}"
	echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
	cd "${srcdir}/${_gitname}"

	install -Dm 644 hooks/colors "${pkgdir}/usr/lib/initcpio/hooks/colors"
	install -Dm 644 install/colors "${pkgdir}/usr/lib/initcpio/install/colors"

	install -Dm 644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
