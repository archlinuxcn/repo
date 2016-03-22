# Maintainer: Gordian Edenhofer <gordian.edenhofer[at]yahoo[dot]de>
# Submitter: Martin Wimpress <code@flexion.org>

pkgname=paper-gtk-theme-git
_pkgname=paper-gtk-theme
pkgver=215.bdca59f
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

build() {
	cd "${srcdir}/${_pkgname}"

	chmod +x ./autogen.sh
	./autogen.sh
	make
}

package() {
	cd "${srcdir}/${_pkgname}"

	make DESTDIR="${pkgdir}" install
}
