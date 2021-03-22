# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=6.0.2
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('x86_64' 'armv7h' 'aarch64')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=('bash' 'python')
provides=('teleport' 'tctl' 'tsh')
install=teleport.install

source=("teleport.service"
        "teleport@.service"
        "teleport.install")

source_x86_64=("teleport-bin-${pkgver}-x86_64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz")
source_armv7h=("teleport-bin-${pkgver}-armv7h.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz")
source_aarch64=("teleport-bin-${pkgver}-aarch64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm64-bin.tar.gz")

sha256sums=('22fd1ee136e9422458740811c9946de447105f26e87dbbc8daa35d17bd1f3894'
            '21ca4e56c9c5e1ce11570894e85ded853e26e91cc2e16ed9114b3d6a2c5c22ef'
            'cff4e3c69677210bdde9a781146df06fba3a62cef72ed6854cd1923a05444435')
sha256sums_x86_64=('a306df00c716dff9bb9535e1670b05246fdb86acb587dfffa7bb01d8c9f914e1')
sha256sums_armv7h=('c1ad9040421ddd682d6610690988ce0bb832881de5048160376a78a3a2775a5f')
sha256sums_aarch64=('1b422158a7a2e60b9b70711669a190d75d9e76438891ab7f83213bba9f5482c6')

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
