# Maintainer: OriginCode <origincoder@yahoo.com>

pkgname=shadowsocks-libev-qrcode
pkgver=r12.cf20ba5
pkgrel=1
pkgdesc="Generate QR code from a shadowsocks-libev config file."
arch=('any')
url="https://github.com/OriginCode/shadowsocks-libev-qrcode"
license=('WTFPL')
depends=(
	'python-qrcode'
	'python-argparse'
)
makedepends=()
provides=('ss-qrcode')
conflicts=()
source=('git+https://github.com/OriginCode/shadowsocks-libev-qrcode')
md5sums=('SKIP')

package() {
	install -d "${pkgdir}/usr/bin"
	cp "${srcdir}/${pkgname}/ss-qrcode" "${pkgdir}/usr/bin"
}
