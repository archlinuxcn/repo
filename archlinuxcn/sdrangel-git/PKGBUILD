# Maintainer: nemanjan00 <nemanjan00+aur@gmail.com>
# Contributor: Filipe Laíns (FFY00) <filipe.lains@gmail.com>
# Contributor: Michal Krenek (Mikos) <m.krenek@gmail.com>

_pkgname=sdrangel
pkgname=$_pkgname-git
pkgver=7.22.5.r52.89e392e91
pkgrel=1
pkgdesc='Qt5/OpenGL SDR and signal analyzer frontend.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='https://github.com/f4exb/sdrangel'
license=('GPL3')
depends=('pkg-config' 'log4cpp' 'opencv' 'fftw'
         'cm256cc' 'dsdcc' 'pulse-native-provider' 'lz4' 'nanomsg'
         'qt5-base' 'qt5-multimedia' 'qt5-websockets' 'qt5-tools' 'qt5-charts' 'qt5-quickcontrols' 'qt5-quickcontrols2'
         'qt5-serialport' 'qt5-declarative' 'qt5-location' 'qt5-speech' 'qt5-webengine' 'qt5-gamepad' 'qt5-svg' 'qt5-graphicaleffects')

# libsigmf requires the vendored version at https://github.com/f4exb/libsigmf/tree/new-namespaces, which isn't packaged yet
makedepends=('git' 'cmake' 'boost' 'doxygen' 'graphviz'
             'ffmpeg' 'libdab' 'zlib' 'faad2' 'sgp4' 'aptdec' 'codec2'
             'libmirisdr4' 'rtl-sdr' 'hackrf' 'libiio' 'limesuite' 'bladerf' 'libperseus-sdr' 'airspy' 'airspyhf' 'libxtrx' 'libuhd')
optdepends=('ffmpeg: DATV demodulator'
            'libdab: DAB demodulator'
            'zlib: DAB demodulator'
            'faad2: DAB demodulator'
            'sgp4: satellite tracker'
            'aptdec: APT (weather satellite) decoder'
            'codec2: FreeDV modulator/demodulator'

            'libmirisdr4<2.0.0: SDRPlay support'
            'rtl-sdr: RTLSDR support'
            'hackrf: HackRF support'
            'libiio: PlutoSDR support'
            'limesuite: LimeSDR support'
            'bladerf: BladeRF support'
            'libperseus-sdr: Perseus SDR support'
            'airspy: Airspy support'
            'airspyhf: Airspy HF+ support'
            'libxtrx: XTRX SDR support'
            'libuhd: USRP support'
)
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("git+$url")
sha512sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	git describe --long --tags | sed 's/^v//;s/\([^-]*-\)g/r\1/;s/-/./g;s/\.rc./rc/g'
}

prepare() {
	cd "$_pkgname"

}

build() {
	# https://bugs.gentoo.org/704322
	export CXXFLAGS="$CXXFLAGS -fpermissive"
	cmake -B build -S "$_pkgname" \
		-Wno-dev \
		-DARCH_OPT="" \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DLIBDSDCC_INCLUDE_DIR=/usr/include/dsdcc \
		-DCM256CC_INCLUDE_DIR=/usr/include/cm256cc

	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir" install
}

# vim: set noet ts=4
