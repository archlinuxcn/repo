# Maintainer: cubercsl <2014cais01 at gmail dot com>
# Maintainer: Integral <integral at member dot fsf dot org>

pkgname=dae-avx2-bin
_pkgname=dae
pkgver=1.1.0rc1
pkgrel=1
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF (with AVX2 CPU optimizations)"
arch=('x86_64')
url="https://github.com/daeuniverse/${_pkgname}"
license=('AGPL-3.0-or-later')
depends=('v2ray-geoip' 'v2ray-domain-list-community')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
replaces=('dae-bin-x64-v3')
backup=("etc/${_pkgname}/config.${_pkgname}")
source=(
	"${pkgname}-${pkgver}.zip::${url}/releases/download/v${pkgver}/${_pkgname}-linux-x86_64_v3_avx2.zip"
	"https://raw.githubusercontent.com/daeuniverse/${_pkgname}/refs/tags/v${pkgver}/install/empty.${_pkgname}"
)
install="${pkgname}.install"
sha256sums=('5cd96c1ebdd1de51a7105e5e221b0564680c143635ad098ee3fb96bab15aef94'
            '8c3b3e962bc1288394e54122e5da8d4d54994d17af2fd290331c464dc6b75c86')

package() {
	# Install binary
	install -vDm755 "${_pkgname}-linux-x86_64_v3_avx2" "${pkgdir}/usr/bin/${_pkgname}"

	# Install systemd service
	install -vDm644 "${_pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"

	# Install exmaple config
	install -vDm644 "example.${_pkgname}" -t "${pkgdir}/etc/${_pkgname}/"

	# Install empty config
	install -vDm640 "empty.${_pkgname}" "${pkgdir}/etc/${_pkgname}/config.${_pkgname}"

	# Create symbolic links for geoip.dat & geosite.dat
	install -d "${pkgdir}/usr/share/${_pkgname}/"
	ln -vs /usr/share/v2ray/geoip.dat "${pkgdir}/usr/share/${_pkgname}/geoip.dat"
	ln -vs /usr/share/v2ray/geosite.dat "${pkgdir}/usr/share/${_pkgname}/geosite.dat"
}
