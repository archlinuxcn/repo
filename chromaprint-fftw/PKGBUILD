# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

# Chromaprint (uses fftw for FFT calculations instead of ffmpeg)

_srcname="chromaprint"
pkgname=chromaprint-fftw
pkgver=1.3.2
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
sha256sums=('c3af900d8e7a42afd74315b51b79ebd2e43bc66630b4ba585a54bf3160439652')

build() {
	cd "$_srcname"-"$pkgver"
	
	cmake \
            -DBIN_INSTALL_DIR:PATH=/usr/bin \
            -DBUILD_SHARED_LIBS:BOOL=ON \
            -DBUILD_EXAMPLES:BOOL=OFF \
            -DBUILD_TESTS:BOOL=OFF \
            -DCMAKE_BUILD_TYPE:STRING=Release \
            -DCMAKE_INSTALL_PREFIX:PATH=/usr \
            -DEXEC_INSTALL_PREFIX:PATH=/usr \
            -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
            -DWITH_AVFFT:BOOL=OFF \
            -DWITH_FFTW3:BOOL=ON \
            -DWITH_KISSFFT:BOOL=OFF \
            -DWITH_VDSP:BOOL=OFF \
            -Wno-dev \
            .
	make
	
}

package() {
	cd "$_srcname"-"$pkgver"
	make DESTDIR="$pkgdir/" install
}
