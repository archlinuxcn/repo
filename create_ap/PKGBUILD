# Maintainer: NicoHood <aur {at} nicohood {dot} de>
# Contributor: Xiaoxiao Pu <i@xiaoxiao.im>

pkgname=create_ap
pkgver=0.4.2
pkgrel=1
pkgdesc="A shell script to create a NATed/Bridged Software Access Point"
arch=('any')
url="https://github.com/oblique/create_ap"
license=('BSD')
depends=('bash' 'hostapd' 'iproute2' 'iw' 'dnsmasq'
         'iptables' 'util-linux' 'procps-ng')
optdepends=('haveged: boost low entropy')
makedepends=('')
backup=('etc/create_ap.conf')
source=("https://github.com/oblique/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('4c252ad17f07a36cee82bb1b6b49d4f7024b32d52e80b4e95d77b70803575005e37ee086c161d12070722de1a250fcb76cca6165792302869fd27b69ceca93b3')

package() {
    make -C "${pkgname}-${pkgver}" DESTDIR="${pkgdir}" install
    install -Dm 644 "${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
