# Maintainer: OriginCode <origincoder@yahoo.com>

pkgname=shadowsocks-libev-qrcode
pkgver=r18.cb9dcb0
pkgrel=1
pkgdesc="Generate QR code from a shadowsocks-libev config file."
arch=('any')
url="https://github.com/OriginCode/shadowsocks-libev-qrcode"
license=('WTFPL')
depends=(
	'python-qrcode'
	'python-argparse'
)
makedepends=('git')
provides=('ss-qrcode')
source=('git+https://github.com/OriginCode/shadowsocks-libev-qrcode')
md5sums=('SKIP')

pkgver() {
        cd "$srcdir/$pkgname"
        printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	install -d "${pkgdir}/usr/bin"
	cp "${srcdir}/${pkgname}/ss-qrcode" "${pkgdir}/usr/bin"
}
