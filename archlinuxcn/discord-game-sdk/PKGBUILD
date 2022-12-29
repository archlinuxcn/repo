# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=discord-game-sdk
pkgver=3.2.1
pkgrel=1
_commit=48d3c2d324796d8236355262ace3b22c1d29acb0
pkgdesc='Discord game SDK'
arch=('x86_64')
url='https://discord.com/developers/docs/game-sdk/sdk-starter-guide'
license=('custom')
depends=('gcc-libs')
options=('!strip')
source=("${pkgname}-${pkgver}.zip"::"https://dl-game-sdk.discordapp.net/${pkgver}/${pkgname//-/_}.zip"
        'DEVELOPER-POLICY'::"https://raw.githubusercontent.com/discord/discord-api-docs/${_commit}/docs/policies_and_agreements/Developer_Policy.md"
        'DEVELOPER-TERMS-OF-SERVICE'::"https://raw.githubusercontent.com/discord/discord-api-docs/${_commit}/docs/policies_and_agreements/Developer_Terms_of_Service.md"
        'STORE-DISTRIBUTION-AGREEMENT-FOR-DEVELOPERS'::"https://raw.githubusercontent.com/discord/discord-api-docs/${_commit}/docs/policies_and_agreements/Store_Distribution_Agreement.md")
noextract=("${pkgname}-${pkgver}.zip")
sha256sums=('6757bb4a1f5b42aa7b6707cbf2158420278760ac5d80d40ca708bb01d20ae6b4'
            '85eb91d7b0e3a1e59e6332073ebd4c7e68ff89373a40ff4a54a874fc63035e3c'
            '991cbb323d4877c536ebb3804c954d3b65480347bfe34aa1680c9e2dca73227e'
            '17cfecb7ffd30aa736d54b8dde6db79babd1b26112a8f14a8d1790055351fdd5')

prepare() {
    mkdir -p "${pkgname}-${pkgver}"
    bsdtar -xf "${pkgname}-${pkgver}.zip" -C "${pkgname}-${pkgver}"
}

package() {
    install -d -m755 "${pkgdir}/usr/src"
    install -D -m644 "${pkgname}-${pkgver}/lib/${CARCH}/${pkgname//-/_}.so" -t "${pkgdir}/usr/lib"
    install -D -m644 "${pkgname}-${pkgver}/README.md" -t "${pkgdir}/usr/share/doc/${pkgname}"
    install -D -m644 {DEVELOPER-{POLICY,TERMS-OF-SERVICE},STORE-DISTRIBUTION-AGREEMENT-FOR-DEVELOPERS} -t "${pkgdir}/usr/share/licenses/${pkgname}"
    cp -dr --no-preserve='ownership' "${pkgname}-${pkgver}/c" "${pkgdir}/usr/include"
    cp -dr --no-preserve='ownership' "${pkgname}-${pkgver}/cpp" "${pkgdir}/usr/src/${pkgname}"
}
