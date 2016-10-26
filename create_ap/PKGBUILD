# Maintainer: NicoHood <aur {at} nicohood {dot} de>
# Contributor: Xiaoxiao Pu <i@xiaoxiao.im>

pkgname=create_ap
pkgver=0.4
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
sha512sums=('42fe72aa06c0f2c5e5156276281b93a97954ca3f32e9f315a09d40b4abf2169a0dd1089fe993110f6b39b09661df8a4d9da46ed46b125d9beca2673faaa35a40')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "create_ap" "${pkgdir}/usr/bin/create_ap"
    install -Dm644 "create_ap.conf" "${pkgdir}/etc/create_ap.conf"
    install -Dm644 "bash_completion" "${pkgdir}/usr/share/bash-completion/completions/create_ap"
    install -Dm644 "create_ap.service" "${pkgdir}/usr/lib/systemd/system/create_ap.service"
    install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

    # TODO requires makefile patch
    #make DESTDIR="${pkgdir}" install
}
