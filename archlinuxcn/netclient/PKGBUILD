# Maintainer: SiHuan <sihuan at sakuya.love>
pkgname=netclient
pkgver=0.10.0
pkgrel=1
pkgdesc="A component of netmaker"
arch=(x86_64)
url='https://github.com/gravitl/netmaker'
license=("custom:SSPL")
depends=('wireguard-tools')
makedepends=('go')

source=("${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('7f0d32448f26f057cb9104589946f579841183edb9c5e37d9f031780b44e7285')

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
