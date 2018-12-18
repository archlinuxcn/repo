# Maintainer: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Co-Maintainer: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>
# Co-Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>

pkgname=teleport-bin
pkgver=3.1.0
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
sha256sums_x86_64=('be9ccfbcf6863f4b3a11e2f36ad6d70ce93f414e3d28ba7b3a7bbacbc3b0af10'
                   '3e332207cfa984a531044d47fde379a9c242aa92e0fef7804a031dff865396dc')
sha256sums_arm=('2bf2244dca052a848ff41ee9c50b0d18d754daeb8107f20036d39b5a5e7ae5b5'
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
