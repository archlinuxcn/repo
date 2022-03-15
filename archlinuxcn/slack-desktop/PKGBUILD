# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Simon Gomizelj <simongmzlj(at)gmail(dot)com>
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=slack-desktop
pkgver=4.24.0
pkgrel=1
pkgdesc="Slack Desktop (Beta) for Linux"
arch=('x86_64')
url="https://slack.com/downloads"
license=('custom')
depends=('gtk3' 'libsecret' 'libxss' 'nss' 'xdg-utils')
optdepends=('libappindicator-gtk3: Systray indicator support'
            'org.freedesktop.secrets: Keyring password store support')
source=("https://downloads.slack-edge.com/releases/linux/${pkgver}/prod/x64/${pkgname}-${pkgver}-amd64.deb"
        "${pkgname}.patch")
noextract=("${pkgname}-${pkgver}-amd64.deb")
b2sums=('d8dccf8b45f78d34f7ac96e97dd6a740718b9572fb51ee5fcbaed0a2b2cd492e7054836acf9540e7ba22d4770baf0607e2fe1fd5d940d3854c098b4429863bd9'
        'b5786265fcaf85be4134a444d5c2376f3b3753b667ac8b5237d74cbc643433148ec0a4f8ddfe65276d6029cc6941b464938e6c37f904c2369cbe14ca3f1819dd')

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
