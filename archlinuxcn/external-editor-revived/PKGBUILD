# Maintainer: Frederick Zhang <frederick888@tsundere.moe>

pkgname=external-editor-revived
pkgver=1.0.0
pkgrel=1
pkgdesc="External Editor Revived is a Thunderbird MailExtension which allows editing emails in programs such as Vim, Neovim, Emacs, etc."
arch=('x86_64')
url="https://github.com/Frederick888/external-editor-revived"
license=('GPL3')
depends=('thunderbird>=91')
makedepends=('rust' 'zip')
source=(
    "https://github.com/Frederick888/external-editor-revived/archive/refs/tags/v${pkgver}.tar.gz"
    "external_editor_revived.json"
)
md5sums=('94f71acfbddb16ea49e50de446064c6d'
         '7e14ff6bb5cad780110f056e5c0d7d34')
sha256sums=('c6882816ef2c405528935019eb49ac0caed868b731ff2fb834ea056882a04406'
            'a4b61c37f16f392f8289002c0e9afc5a8570d7ed902be25c62c7dc0703a20e05')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    cargo build --locked --release --target-dir ./target
    cd "${srcdir}/${pkgname}-${pkgver}/extension"
    zip -r -FS "${srcdir}/${pkgname}@tsundere.moe.xpi" *
}

package() {
    cd "${srcdir}"
    install -d "${pkgdir}/usr/lib/thunderbird/extensions"
    install -Dm644 "${pkgname}@tsundere.moe.xpi" "${pkgdir}/usr/lib/thunderbird/extensions/${pkgname}@tsundere.moe.xpi"

    install -d "${pkgdir}/usr/lib/mozilla/native-messaging-hosts"
    install -Dm644 "external_editor_revived.json" "${pkgdir}/usr/lib/mozilla/native-messaging-hosts/external_editor_revived.json"

    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

    install -d "${pkgdir}/usr/share/license/${pkgname}"
    install -Dm644 "LICENSE" "${pkgdir}/usr/share/license/${pkgname}/LICENSE"
}
