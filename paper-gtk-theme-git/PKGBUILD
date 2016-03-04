# Maintainer: Gordian Edenhofer <gordian.edenhofer[at]yahoo[dot]de>
# Submitter: Martin Wimpress <code@flexion.org>

pkgname=paper-gtk-theme-git
_pkgname=paper-gtk-theme
pkgver=188.617a6b1
pkgrel=1
pkgdesc="A modern desktop theme suite. Its design is mostly flat with a minimal use of shadows for depth."
arch=('any')
url="http://samuelhewitt.com/paper/theme"
license=('GPL3')
depends=('gtk-engine-murrine')
# Optional dependencies for developers
#optdepends=("python: scripts to simplify the rendering process"
#	"inkscape: edit theme assets")
makedepends=('git')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${_pkgname}"::"git+https://github.com/snwh/${_pkgname}.git")
md5sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_pkgname}"
	echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
	cd "${srcdir}/${_pkgname}"

	install -dm755 "${pkgdir}"/usr/share/themes/Paper
	cp -dpr --no-preserve=ownership ./Paper "${pkgdir}"/usr/share/themes/

	# Developer scripts explicitly not for end users
	#install -dm755 "${pkgdir}"/usr/share/"${_pkgname}"
	#cp -dpr --no-preserve=ownership ./*.py "${pkgdir}"/usr/share/"${_pkgname}"
	#cp -dpr --no-preserve=ownership ./src "${pkgdir}"/usr/share/"${_pkgname}"
}
