# Maintainer: Gordian Edenhofer <gordian.edenhofer[at]yahoo[dot]de>
# Submitter: Martin Wimpress <code@flexion.org>

pkgname=paper-gtk-theme-git
_pkgname=paper-gtk-theme
pkgver=244.de443e3
pkgrel=1
pkgdesc="A modern desktop theme suite. Its design is mostly flat with a minimal use of shadows for depth."
arch=('any')
url="http://samuelhewitt.com/paper/theme"
license=('GPL3')
optdepends=("gtk-engine-murrine: gtk2 bindings"
	"gtk3: gtk3 bindings")
# Optional dependencies for developers
#optdepends=("python: scripts to simplify the rendering process"
#	"inkscape: recommended editing software for theme assets")
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
