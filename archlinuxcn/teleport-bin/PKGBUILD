# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=5.0.1
pkgrel=2
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('x86_64' 'armv7')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=('bash' 'python')
provides=('teleport' 'tctl' 'tsh')
install=teleport.install

source=("teleport.service"
        "teleport@.service"
        "teleport.install")

source_x86_64=("teleport-bin-${pkgver}-${CARCH}.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz")

source_armv7=("teleport-bin-${pkgver}-${CARCH}.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz")

sha256sums=('22fd1ee136e9422458740811c9946de447105f26e87dbbc8daa35d17bd1f3894'
            '21ca4e56c9c5e1ce11570894e85ded853e26e91cc2e16ed9114b3d6a2c5c22ef'
            'cff4e3c69677210bdde9a781146df06fba3a62cef72ed6854cd1923a05444435')
sha256sums_x86_64=('f25dcc0d04fa5085cc111c537e76e87321797160ea27f8f7efd6de08d531898d')
sha256sums_armv7=('f25dcc0d04fa5085cc111c537e76e87321797160ea27f8f7efd6de08d531898d')

options=(!strip)

package() {
    install -Dm644 ${srcdir}/teleport.service "${pkgdir}/usr/lib/systemd/system/teleport.service"
    install -Dm644 ${srcdir}/teleport.service "${pkgdir}/usr/lib/systemd/system/teleport@.service"
    install -dm755 "${pkgdir}/etc/teleport"

    cd "${srcdir}/teleport"
    install -Dm755 teleport "${pkgdir}/usr/bin/teleport"
    install -Dm755 tctl "${pkgdir}/usr/bin/tctl"
    install -Dm755 tsh "${pkgdir}/usr/bin/tsh"

    cp -r examples "${pkgdir}/etc/teleport/"
}
