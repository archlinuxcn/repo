# Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>
# Maintainer: Maarten de Boer <maarten@cloudstek.nl>
# Maintainer: Christian Heusel <christian@heusel.eu>
# Contributor: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Contributor: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>

_pkgname=teleport
pkgname=teleport-bin
pkgver=11.3.2
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('i386' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=()
provides=('teleport' 'tctl' 'tsh' 'tbot')
install=teleport.install

source=("teleport.service"
        "teleport@.service"
        "teleport.install")

source_i386=("teleport-bin-${pkgver}-i386.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-386-bin.tar.gz")
source_x86_64=("teleport-bin-${pkgver}-x86_64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz")
source_armv7h=("teleport-bin-${pkgver}-armv7h.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz")
source_aarch64=("teleport-bin-${pkgver}-aarch64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm64-bin.tar.gz")

sha256sums=('22fd1ee136e9422458740811c9946de447105f26e87dbbc8daa35d17bd1f3894'
            '21ca4e56c9c5e1ce11570894e85ded853e26e91cc2e16ed9114b3d6a2c5c22ef'
            'ce2dd61cae3c0c3684e7e629f98b77551e66ddedca2194250a34f0efbc674f3a')
sha256sums_i386=('b9eddf441511b088fcbf27db7065947ff3535b769a012bdd7f78a1647de5a9d5')
sha256sums_x86_64=('a89bd589102b59942afdc5b1e686adfc2d80fe6f3f8af96eadfedb324f4dccb0')
sha256sums_armv7h=('5d41130700e4fbb49a9cd705e309025f9f060b03dfbfcc8c61402babc98155e8')
sha256sums_aarch64=('0d1f904ed12fbfbfb2e2ff1995011ff8de198b82283253b760fe9b0f0147bd91')

options=(!strip)

package() {
    cd "${srcdir}/${_pkgname}"

    # Install binaries
    install -Dm755 teleport "${pkgdir}/usr/bin/teleport"
    install -Dm755 tctl "${pkgdir}/usr/bin/tctl"
    install -Dm755 tsh "${pkgdir}/usr/bin/tsh"
    install -Dm755 tbot "${pkgdir}/usr/bin/tbot"

    # Install services
    install -Dm644 ${srcdir}/teleport.service "${pkgdir}/usr/lib/systemd/system/teleport.service"
    install -Dm644 ${srcdir}/teleport@.service "${pkgdir}/usr/lib/systemd/system/teleport@.service"

    # Copy example files
    install -dm755 "${pkgdir}/usr/share/teleport"
    cp -r examples "${pkgdir}/usr/share/teleport/"
}
