# Maintainer: Integral <integral@member.fsf.org>

pkgname=daed-avx2-bin
_pkgname=daed
pkgver=1.21.1
pkgrel=1
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core) (with AVX2 CPU optimizations)"
url="https://daeuniverse.github.io/daed"
arch=('x86_64')
license=('AGPL-3.0-or-later AND MIT')
depends=('v2ray-geoip' 'v2ray-domain-list-community')
provides=("${_pkgname}" "dae")
conflicts=("${_pkgname}" "${_pkgname}-git" "dae")
replaces=('daed-bin-x64-v3')
source=("${pkgname}-${pkgver}.zip::https://github.com/daeuniverse/${_pkgname}/releases/download/v${pkgver}/${_pkgname}-linux-x86_64_v3_avx2.zip"
       "${_pkgname}-${pkgver}-LICENSE::https://raw.githubusercontent.com/daeuniverse/daed/v${pkgver}/LICENSE")
install="${pkgname}.install"
sha512sums=('25cd258bc1b261f5b23523bdb52555a002e23e20fae159b6130c8ba8d0dc64d0c32610377518330bcdd59d5332cf8bfa8043b88e22ca5063fedac76f0c03ee0a'
            '82e50adf3228132f787522c8562b8b85958ce3f33b76445c148e2517c937b62999d3b4594ee1adc9bbe473619840b181ea984a34772c9f65fd592847e621fd66')

package() {
	# Install license
	install -vDm644 "${_pkgname}-${pkgver}-LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

	cd "${_pkgname}-linux-x86_64_v3_avx2/"

	# Install binary
	install -vDm755 "${_pkgname}-linux-x86_64_v3_avx2" "${pkgdir}/usr/bin/${_pkgname}"

	# Install systemd service
	install -vDm644 "${_pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"

	# Create symbolic links for geoip.dat & geosite.dat
	install -d "${pkgdir}/usr/share/${_pkgname}/"
	ln -vs "/usr/share/v2ray/geoip.dat" "${pkgdir}/usr/share/${_pkgname}/geoip.dat"
	ln -vs "/usr/share/v2ray/geosite.dat" "${pkgdir}/usr/share/${_pkgname}/geosite.dat"
}
