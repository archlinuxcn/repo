# Maintainer: gbr <gbr at pm dot me>

_pkgname=notes
pkgname=notes-git
pkgver=2.2.0.r2.g67e724f
pkgrel=2
pkgdesc='Note taking application, write down your thoughts'
arch=('x86_64')
url='https://github.com/nuttyartist/notes'
license=('MPL')
makedepends=('cmake' 'git')
depends=('hicolor-icon-theme' 'qt6-base' 'qt6-declarative' 'qt6-quick3d')
provides=('notes')
conflicts=('notes')
source=("${pkgname}::git+https://github.com/nuttyartist/notes"
	'git+https://github.com/b00f/qautostart.git'
	'git+https://github.com/pbek/qmarkdowntextedit.git'
	'git+https://github.com/alex-spataru/QSimpleUpdater.git')
sha256sums=('SKIP'
	'SKIP'
	'SKIP'
	'SKIP')

pkgver() {
	cd "${pkgname}"
	git describe --long --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "${pkgname}"
	git submodule init
	git submodule set-url 3rdParty/qautostart "${srcdir}/qautostart"
	git submodule set-url 3rdParty/qmarkdowntextedit "${srcdir}/qmarkdowntextedit"
	git submodule set-url 3rdParty/QSimpleUpdater "${srcdir}/QSimpleUpdater"
	git -c protocol.file.allow=always submodule update
}

build() {
	cd "${pkgname}"
	cmake -B build \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DUSE_QT_VERSION=6 \
		-DUPDATE_CHECKER=OFF \
		-DGIT_REVISION=ON
	cmake --build build
}

package() {
	cd "${pkgname}"
	DESTDIR="${pkgdir}" cmake --install build
}
