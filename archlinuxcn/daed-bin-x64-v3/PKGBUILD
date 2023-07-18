# Maintainer: Integral <integral@murena.io>

pkgname=daed-bin-x64-v3
_pkgname=daed
pkgver=0.2.0
pkgrel=3
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core)."
url="https://daeuniverse.github.io/daed"
arch=('x86_64')
license=('AGPL' 'MIT')
provides=('daed')
conflicts=('daed' 'daed-git')
source=("${pkgname}-${pkgver}.zip::https://github.com/daeuniverse/${_pkgname}/releases/download/v${pkgver}/${_pkgname}-linux-x86_64_v3_avx2.zip")
sha512sums=('bae701ef46e7f6332b87a441a7dfbafc2f9324fef1a74df30b238d7f9e43e98f49a09dc1cabd3b78adbb2f524e30392c3b5e2d629a72d5b66deecb690315c584')

prepare() {
	if !(/lib/ld-linux-x86-64.so.2 --help | grep "x86-64-v3 (supported, searched)" &> /dev/null); then
		echo "Your CPU does NOT support x86-64-v3!"
		echo "Exiting..."
		exit 1
	fi
}

package() {
	# Install binary
	mv "daed-linux-x86_64_v3_avx2" "${_pkgname}"
	install -vDm755 "${_pkgname}" -t "${pkgdir}/usr/bin/"

	# Install systemd service
	install -vDm644 "daed.service" -t "${pkgdir}/usr/lib/systemd/system/"

	# Install geoip.dat & geosite.dat
	install -vDm644 "geoip.dat" -t "${pkgdir}/usr/share/${_pkgname}/"
	install -vDm644 "geosite.dat" -t "${pkgdir}/usr/share/${_pkgname}/"

	echo "After installation completed, open your browser and navigate to http://localhost:2023"
}
