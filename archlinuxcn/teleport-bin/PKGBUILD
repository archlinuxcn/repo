# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=4.3.0
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('x86_64' 'armv7')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=('bash' 'python')
install=teleport.install

source=("teleport.service"
        "teleport.install")

source_x86_64=("teleport-bin-${pkgver}-${CARCH}.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz")

source_armv7=("teleport-bin-${pkgver}-${CARCH}.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz")

sha256sums=('78e272d3c6bb255fd254e38a3237b808f6e588bd4861f233eca010189e95a7e2'
            'cff4e3c69677210bdde9a781146df06fba3a62cef72ed6854cd1923a05444435')
sha256sums_x86_64=('9ebad4e52271074c218f18022f5199857c7144583be490ec72bf517f98215cae')
sha256sums_armv7=('9ebad4e52271074c218f18022f5199857c7144583be490ec72bf517f98215cae')

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
