# Maintainer: Alfredo Ramos <alfredo dot ramos at yandex dot com>
# Contributor: Arthur Țițeică arthur.titeica/gmail/com
# Contributor: Thomas Laube <tomx3@tomtomtom.org>

_pkgname=vokoscreen
pkgname=${_pkgname}-git
pkgver=2.9.3.beta.35.gb763020
pkgrel=1
pkgdesc='An easy to use screencast creator. Development version.'
arch=('i686' 'x86_64')
url='http://linuxecke.volkoh.de/vokoscreen/vokoscreen.html'
license=('GPL2')

depends=(
	'qt5-x11extras' 'qt5-multimedia' 'qt-gstreamer'
	'gst-plugins-good' 'gst-plugins-bad' 'pulseaudio-alsa'
)
makedepends=('git' 'qt5-tools' 'libxrandr')
optdepends=('gst-plugins-ugly: for x264 video codec')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")

source=(
	"git+https://github.com/vkohaupt/${_pkgname}NG.git"
	'install.pri'
)
sha512sums=(
	'SKIP'
	'0a5e0523adaa9e7f9b46cbbc8f7d8d0167787b67f11cfb7895785e3f93ab8836526c1b0891f4bf3362f4e8bc44885ffcf99670b86558aa667bd4f4ac7df56f11'
)

pkgver() {
	# Updating package version
	cd "${srcdir}"/${_pkgname}NG
	git describe --long --tags 2>/dev/null | sed -r 's/-/./g'
}

prepare() {
	cd "${srcdir}"/${_pkgname}NG

	# Add install instructions
	cp ../install.pri src/
	echo 'include(install.pri)' >> src/vokoscreen.pro

	# Create build directory
	mkdir -p "${srcdir}"/build
}

build() {
	# Building package
	cd "${srcdir}"/build
	qmake-qt5 ../${_pkgname}NG/src \
		QMAKE_CFLAGS="${CFLAGS}" \
		QMAKE_CXXFLAGS="${CXXFLAGS}" \
		CONFIG+=release \
		CONFIG+=c++14
	make
}

package() {
	# Installing package
	cd "${srcdir}"/build
	make INSTALL_ROOT="${pkgdir}" install
}
