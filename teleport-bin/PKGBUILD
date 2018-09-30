# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=2.7.5
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('x86_64' 'arm')
url="https://github.com/gravitational/teleport"
license=('Apache')
depends=('glibc')
install=teleport.install
source_x86_64=(
    "https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz"
    "teleport.service"
    )
sha256sums_x86_64=('2f3ce6f1a38cdb712954d3e4a605c070060a55d92a12c0cb03f8a208a1764250'
                   '3e332207cfa984a531044d47fde379a9c242aa92e0fef7804a031dff865396dc')
sha256sums_arm=('500e140a1dec5a05f16beb8cee321934a2fa8308db6a4e43139a0fd5fb1e6e66'
                '3e332207cfa984a531044d47fde379a9c242aa92e0fef7804a031dff865396dc')
source_arm=(
    "https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz"
    "teleport.service"
    )
options=(!strip)

package() {
    mkdir -p "${pkgdir}/usr/lib/systemd/system" "${pkgdir}/usr/bin"
    install -m644 -t "${pkgdir}/usr/lib/systemd/system/" teleport.service
    cd "${srcdir}/teleport"
    install -m755 -t "${pkgdir}/usr/bin/" teleport tctl tsh
    # no man pages, docs or web assets in release tarball
}
