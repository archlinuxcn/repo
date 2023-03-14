# Contributor: Integral <integral@murena.io>
pkgname=klevernotes-git
_pkgname=klevernotes
pkgver=0.1_r103.gc820241
pkgrel=2
pkgdesc="A convergent markdown note taking application."
url="https://invent.kde.org/office/klevernotes"
arch=('x86_64')
license=('GPL' 'LGPL' 'BSD')
groups=('kde-applications-git' 'kde-utilities-git')
depends=('kio' 'qt5-webengine')
makedepends=('extra-cmake-modules' 'git')
source=("git+https://invent.kde.org/office/klevernotes.git")
md5sums=('SKIP')

pkgver() {
	cd ${_pkgname}/
	_version=$(grep -m1 "${_pkgname} VERSION" CMakeLists.txt | awk '{print $3}' | sed 's/)//')
	echo "${_version}_r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

prepare() {
	install -d build/
}

build() {
	cd build/
	cmake -B build/ -S ../${_pkgname} -DBUILD_TESTING=OFF
	cmake --build build/
}

package() {
	cd build/
	DESTDIR="${pkgdir}/" cmake --install build/

	# Licenses
	install -Dm644 ${srcdir}/${_pkgname}/LICENSES/* -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
