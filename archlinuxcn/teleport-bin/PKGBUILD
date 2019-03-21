# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=3.1.8
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('x86_64' 'arm')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=('bash' 'python')
install=teleport.install

source_x86_64=(
    "https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz"
    "teleport.service"
    "teleport.install"
)

sha256sums_x86_64=('6c862c72dee807b1fb4bc7d5e2e4522e9ddc06b9ffc2c32a9a0b28ea8dfa6e80'
                   '48b27cf06bd88f3121f3febec352269f75e4f30e8e7cd80a72c630b3cf34a5e6'
                   'cff4e3c69677210bdde9a781146df06fba3a62cef72ed6854cd1923a05444435')
sha256sums_arm=('17a22abf5fe2119256705efd04bf0ae036dbdf980b9028ed03e563cf7180d434'
                '48b27cf06bd88f3121f3febec352269f75e4f30e8e7cd80a72c630b3cf34a5e6'
                'cff4e3c69677210bdde9a781146df06fba3a62cef72ed6854cd1923a05444435')
source_arm=(
    "https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz"
    "teleport.service"
    "teleport.install"
)

options=(!strip)

package() {
    install -Dm644 ${srcdir}/teleport.service "${pkgdir}/usr/lib/systemd/system/teleport.service"
    install -dm755 "${pkgdir}/etc/teleport"

    cd "${srcdir}/teleport"
    install -Dm755 teleport "${pkgdir}/usr/bin/teleport"
    install -Dm755 tctl "${pkgdir}/usr/bin/tctl"
    install -Dm755 tsh "${pkgdir}/usr/bin/tsh"

    cp -r examples "${pkgdir}/etc/teleport/"
}
