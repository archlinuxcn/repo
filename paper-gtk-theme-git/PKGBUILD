# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Submitter: Martin Wimpress <code@flexion.org>

pkgname=paper-gtk-theme-git
_pkgname=paper-gtk-theme
pkgver=301.f75724f
pkgrel=1
pkgdesc="A modern desktop theme suite. Its design is mostly flat with a minimal use of shadows for depth."
arch=('any')
url="https://snwh.org/paper"
license=('GPL3')
optdepends=("gtk-engine-murrine: gtk2 bindings"
	"gtk3: gtk3 bindings")
# Optional dependencies for developers
#optdepends=("python: scripts to simplify the rendering process"
#	"inkscape: recommended editing software for theme assets")
makedepends=('git')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
source=("${_pkgname}"::"git+https://github.com/snwh/${_pkgname}.git")
sha512sums=('SKIP')

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
	make -C "${srcdir}/${_pkgname}" DESTDIR="${pkgdir}" install
}
