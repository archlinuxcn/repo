# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

# NOTE:
# If you want the fpcalc utility: add 'ffmpeg' to depends and change '-DBUILD_TOOLS' to 'ON'.
# FFT calculations will still be made using FFTW3. libchromaprint.so will still be free of
# ffmpeg libraries. But the fpcalc utility will be linked against ffmpeg libraries, so be
# warned that this can cause some sort of circular dependency with ffmpeg if your ffmpeg
# build has '--enable-chromaprint'.

_srcname="chromaprint"
pkgname=chromaprint-fftw
pkgver=1.4.2
pkgrel=1
pkgdesc="Extracts fingerprints from any audio source (uses fftw for FFT calculations instead of ffmpeg)"
arch=('i686' 'x86_64')
url="https://acoustid.org/chromaprint"
license=('GPL')
makedepends=('cmake')
depends=('fftw')
provides=('chromaprint' 'libchromaprint.so')
conflicts=('chromaprint' 'chromaprint-git')
source=("https://bitbucket.org/acoustid/chromaprint/downloads/${_srcname}-${pkgver}.tar.gz")
sha256sums=('989609a7e841dd75b34ee793bd1d049ce99a8f0d444b3cea39d57c3e5d26b4d4')

build() {
	cd "$_srcname"-"$pkgver"
	
	cmake \
	    -DBIN_INSTALL_DIR:PATH=/usr/bin \
	    -DBUILD_SHARED_LIBS:BOOL=ON \
	    -DBUILD_TESTS:BOOL=OFF \
	    -DBUILD_TOOLS:BOOL=OFF \
	    -DCMAKE_BUILD_TYPE:STRING=Release \
	    -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
	    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
	    -DEXEC_INSTALL_PREFIX:PATH=/usr \
	    -DFFT_LIB:STRING=fftw3 \
	    -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
	    -Wno-dev \
	    .
	make
}

package() {
	cd "$_srcname"-"$pkgver"
	make DESTDIR="$pkgdir/" install
}
