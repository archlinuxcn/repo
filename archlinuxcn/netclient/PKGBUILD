# Maintainer: SiHuan <sihuan at sakuya.love>
pkgname=netclient
pkgver=0.9.4
pkgrel=1
pkgdesc="A component of netmaker"
arch=(x86_64)
url='https://github.com/gravitl/netmaker'
license=("custom:SSPL")
depends=()
makedepends=('go')

source=("${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('0e730d5218544ae77ad82563d43fbce5db0115d71f1e08620dbebde37ed29b25')

build() {
	cd "$srcdir/netmaker-${pkgver}/${pkgname}"
	go build -ldflags "-s -w"
}

package() {
	cd "$srcdir/netmaker-${pkgver}"
	install -Dm755 "${pkgname}/${pkgname}" "$pkgdir/usr/bin/${pkgname}"
	install -Dm644 "README.md" "$pkgdir/usr/share/doc/${pkgname}/README.md"
	install -Dm644 "LICENSE.txt" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
