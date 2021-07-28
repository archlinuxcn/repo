# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Simon Gomizelj <simongmzlj(at)gmail(dot)com>
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=slack-desktop
pkgver=4.18.0
pkgrel=1
pkgdesc="Slack Desktop (Beta) for Linux"
arch=('x86_64')
url="https://slack.com/downloads"
license=('custom')
depends=('gtk3' 'libsecret' 'libxss' 'nss' 'xdg-utils')
optdepends=('libappindicator-gtk3: Systray indicator support'
            'org.freedesktop.secrets: Keyring password store support')
source=("https://downloads.slack-edge.com/linux_releases/${pkgname}-${pkgver}-amd64.deb"
        "${pkgname}.patch")
noextract=("${pkgname}-${pkgver}-amd64.deb")
sha256sums=('701a8bd2a6c0e793b35092f147dd6639e66a1860ad300088a988f39d45ac0db6'
            'd351d8ff3eee0006d1c66e3efec60a78ae8cc10fd8c3042e8d899125a1c4bf47')

package() {
    bsdtar -O -xf "slack-desktop-${pkgver}"*.deb data.tar.xz | bsdtar -C "${pkgdir}" -xJf -

    # Fix hardcoded icon path in .desktop file
    patch -d "${pkgdir}" -p1 <"${pkgname}".patch

    # Permission fix
    find "${pkgdir}" -type d -exec chmod 755 {} +

    # Remove all unnecessary stuff
    rm -rf "${pkgdir}/etc"
    rm -rf "${pkgdir}/usr/lib/slack/src"
    rm -rf "${pkgdir}/usr/share/lintian"
    rm -rf "${pkgdir}/usr/share/doc"

    # Move license
    install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${pkgdir}/usr/lib/slack/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "/usr/share/licenses/${pkgname}/LICENSE" "${pkgdir}/usr/lib/slack/LICENSE"
}
