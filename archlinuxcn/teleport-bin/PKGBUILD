# Maintainer: Ariel AxionL <arielaxionl@gmail.com | axionl@aosc.io>
# Maintainer: Maarten de Boer <maarten@cloudstek.nl>
# Maintainer: Christian Heusel <christian@heusel.eu>
# Contributor: Johannes Pfrang <johannespfrang+arch @ gmail.com>
# Contributor: Emanuele 'Lele aka eldios' Calo' <xeldiosx@gmail.com>

_pkgname=teleport
pkgname=teleport-bin
pkgver=16.4.3
pkgrel=1
pkgdesc="Modern SSH server for teams managing distributed infrastructure"
arch=('i386' 'x86_64' 'armv7h' 'aarch64')
url="https://goteleport.com/"
license=('LicenseRef-TeleportCommunityLicense')
depends=(glibc gcc-libs)
optdepends=("python: for the examples"
            "bash: for the examples")
provides=('teleport' 'tctl' 'tsh' 'tbot')
conflicts=('teleport')
install=teleport.install

source=("teleport.service"
        "teleport@.service"
        "teleport.install"
        "LICENSE-community::https://raw.githubusercontent.com/gravitational/teleport/master/LICENSE-community")

# The teleport servers do not allow for byte ranges to continue download so we set -C0
# https://aur.archlinux.org/packages/teleport-bin#comment-906339
DLAGENTS=('https::/usr/bin/curl -qgb "" -fL -C0 --retry 3 --retry-delay 3 -o %o %u')

source_i386=("teleport-bin-${pkgver}-i386.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-386-bin.tar.gz")
source_x86_64=("teleport-bin-${pkgver}-x86_64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-amd64-bin.tar.gz")
source_armv7h=("teleport-bin-${pkgver}-armv7h.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm-bin.tar.gz")
source_aarch64=("teleport-bin-${pkgver}-aarch64.tar.gz::https://get.gravitational.com/teleport-v${pkgver}-linux-arm64-bin.tar.gz")

sha256sums=('b7ac1b9fa9788989b9cef9e555b278635faa4be8350a959580f19076241cde85'
            'b7aa05eeb0d39875481c56bc21edf60a5bd7184bc5c424df68a5d4eb2b2882f1'
            'c71bbe70179aceb0f49d2a4f1e0a83da040ca72373e17ca82cc2489cd6e07801'
            'a45b5a4bdfe894ebd901568b29517fe3d8342d49f1f394feb62a8dc8fe233dda')
sha256sums_i386=('1efb42ae3bea7b75c787d7fdfd62aa6cd70376456e57db79a25ab1a908af761d')
sha256sums_x86_64=('f06ae86712f069bd214a3d421d9483e289c055b3e9440f1c4df5c93506c6120f')
sha256sums_armv7h=('012c12f5610a58f9d346923beeb38140922fe62c66744ed684c037a0b0b69da0')
sha256sums_aarch64=('068d582e844d69c036a7f3af8b8dac9171d7b8201bcd0459b4986ab5a00debc3')

options=(!strip)

package() {
    cd "${_pkgname}"

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

    # Install license
    install -Dm644 "${srcdir}/LICENSE-community" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
