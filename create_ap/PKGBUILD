# Maintainer:  Xiaoxiao Pu <i@xiaoxiao.im>

pkgname=create_ap
pkgver=r124.d55adb7
pkgrel=1
pkgdesc="A shell script to create a NATed/Bridged Software Access Point"
arch=('any')
url="https://github.com/oblique/create_ap"
license=('BSD')
depends=('bash' 'hostapd' 'iproute2' 'iw' 'dnsmasq'
         'iptables' 'util-linux')
optdepends=('haveged: boost low entropy')
makedepends=('git')
install=create_ap.install
source=("git+https://github.com/oblique/create_ap")
sha256sums=('SKIP')

pkgver() {
	cd "${srcdir}/create_ap"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "${srcdir}/create_ap/"
	install -Dm755 "create_ap" "${pkgdir}/usr/bin/create_ap"
	install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/create_ap/LICENSE"
	install -Dm644 "create_ap.service" "${pkgdir}/usr/share/doc/create_ap/create_ap.service"
}