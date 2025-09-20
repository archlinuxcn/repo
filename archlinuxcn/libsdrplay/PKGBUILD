# Maintainer: Evgeniy Dombek <edombek@yandex.ru>
# Maintainer: Dan McCurry <dan.mc at protonmail dot com>
# Maintainer: Ethan Best <ethan at totalsecond dot com>
# with special thanks to deadlte for version 3.07.1

pkgname=libsdrplay
pkgver=3.15.2
pkgrel=3
pkgdesc="Modules for the SDRplay receiver"
arch=('aarch64' 'x86_64')
url="http://www.sdrplay.com"
license=('custom:EULA')
depends=('libusb>=1.0')
source=("http://www.sdrplay.com/software/SDRplay_RSP_API-Linux-${pkgver}.run"
		"sdrplay.service"
		"66-sdrplay.rules"
		"20-sdrplay.hwdb")
sha256sums=('3a97ca764263bbe76fb0f2220e6408942357e8864c19e1408a6d6987af382fe3'
			'69935539fad9b7cf2cd1feb4017974cfaf164c37dfd01adfb0086ea7512e6ce7'
			'750e797e330f61d59c108ab8c831e7c2af045f474df3b1934ba3ef283a1a0e97'
			'8c2bda0690fb16d74e4b7836cf4c4a4a725029fed1546a42b7a8ca193eb47c95')

prepare() {
	cd ${srcdir}

	msg2 "Extracting makeself archive..."
	sh SDRplay_RSP_API-Linux-${pkgver}.run --tar xf
}

package() {
	cd "${srcdir}"

	CARCH_=$CARCH
    case ${CARCH} in
     x86_64) CARCH_="amd64" ;;
     aarch64)   CARCH_="arm64" ;;
    esac
	
	msg2 "Getting API version..."
	_apivers=$(sed -n 's/^VERS="\(.*\)"/\1/p' install_lib.sh)
	msg2 "API version: ${_apivers}"

	# These commands are equivalent to the scripts used in the supplied
	# run file
	install -D -m644 sdrplay_license.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -D -m644 "${CARCH_}/libsdrplay_api.so.${_apivers}" 		"${pkgdir}/usr/lib/libsdrplay_api.so.${_apivers}"
	install -D -m755 "${CARCH_}/sdrplay_apiService" "${pkgdir}/usr/bin/sdrplay_apiService"
	install -D -m644 "sdrplay.service" "${pkgdir}/etc/systemd/system/sdrplay.service"

	(cd inc && find . -type f -exec install -D -m644 "{}" "${pkgdir}/usr/include/{}" \;)
		
	install -D -m644 66-sdrplay.rules "${pkgdir}/etc/udev/rules.d/66-sdrplay.rules"
	install -D -m644 20-sdrplay.hwdb "${pkgdir}/etc/udev/hwdb.d/20-sdrplay.hwdb"

	cd "${pkgdir}/usr/lib"
	ln -s libsdrplay_api.so.${_apivers} libsdrplay_api.so.2
	ln -s libsdrplay_api.so.${_apivers} libsdrplay_api.so
	
}
