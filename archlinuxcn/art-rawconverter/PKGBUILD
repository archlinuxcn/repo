# Maintainer: René Wagner <rwa at clttr dot info>
pkgname=art-rawconverter
pkgver=1.20.1
pkgrel=1
pkgdesc="raw image converter ART (forked from RawTherapee with ease of use in mind)"
arch=('i686' 'x86_64' 'aarch64')
url="https://bitbucket.org/agriggio/art/wiki/Home"
license=('GPL3')
depends=('opencolorio' 'lensfun' 'libraw' 'exiv2' 'fftw' 'gtk3' 'glibmm' 'gtkmm3' 'lcms2' 'libcanberra' 'libiptcdata' 'desktop-file-utils' 'mimalloc' 'openmp') 
optdepends=('perl-image-exiftool: metadata support for CR3 images' 'art-rawconverter-imageio: add support for additional image formats' 'lcms2-ff: lcms2 with fast-float plugin for improved export speed' )
makedepends=('pkgconf' 'cmake' 'git' 'gcc' 'hicolor-icon-theme' 'fakeroot')
conflicts=('art-rawconverter-git')
source=("${pkgname}_${pkgver}::git+https://bitbucket.org/agriggio/art.git#tag=${pkgver}")
sha256sums=('SKIP')

build() {
	mkdir -p "$srcdir/${pkgname}_${pkgver}_build"
	cd "$srcdir/${pkgname}_${pkgver}_build"

	cmake "../${pkgname}_${pkgver}" \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE=Release \
	-DPROC_TARGET_NUMBER="2" \
	-DWITH_LTO="ON" \
	-DENABLE_LIBRAW="ON" \
	-DENABLE_OCIO="ON" \
 	-DBUILD_SHARED="ON"

	make
}

package() {
	cd "$srcdir/${pkgname}_${pkgver}_build"
	make DESTDIR="$pkgdir/" install
}
