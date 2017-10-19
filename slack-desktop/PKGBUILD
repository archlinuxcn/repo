# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Simon Gomizelj <simongmzlj(at)gmail(dot)com>
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=slack-desktop
pkgver=2.8.2
pkgrel=3
pkgdesc="Slack Desktop (Beta) for Linux"
arch=('x86_64')
url="https://slack.com/downloads"
license=('custom')
depends=('alsa-lib' 'gconf' 'gtk2' 'libcurl-compat' 'libsecret' 'libxss' 'libxtst' 'nss')
optdepends=('gnome-keyring')
source=("https://downloads.slack-edge.com/linux_releases/${pkgname}-${pkgver}-amd64.deb"
        "${pkgname}.patch")
sha256sums=('75661e19efc7c9760f481a9688e5d6e24a2bdc830bda60ca5ec9876a64fc2f05'
            '5eceb99baa2e248ea8b2785a582de2e6b876e9bf820e818f92c3ae3827ee5fed')

package() {
    bsdtar -O -xf "slack-desktop-${pkgver}"*.deb data.tar.xz | bsdtar -C "${pkgdir}" -xJf -

    # Fix hardcoded icon path in .desktop file
    patch -d "${pkgdir}" -p1 <"${pkgname}".patch

    # Permission fix
    find "${pkgdir}" -type d -exec chmod 755 {} +

    # Remove all unnecessary stuff
    rm -rf "${pkgdir}/etc"
    rm -rf "${pkgdir}/usr/share/lintian"
    rm -rf "${pkgdir}/usr/share/doc"

    # Move license
    install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${pkgdir}/usr/lib/slack/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "/usr/share/licenses/${pkgname}/LICENSE" "${pkgdir}/usr/lib/slack/LICENSE"
}
