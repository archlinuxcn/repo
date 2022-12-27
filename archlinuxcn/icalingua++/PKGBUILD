pkgname=icalingua++
_pkgname=icalingua
pkgver=2.8.3
pkgrel=1
pkgdesc='A branch of deleted Icalingua, with limited support'
license=('AGPL3')
depends=('ffmpeg' 'electron' 'libappindicator-gtk3')
optdepends=('mongodb-bin: Provides storage'
            'redis: Provides storage')
makedepends=('asar')
arch=('aarch64' 'x86_64')
url="https://github.com/Icalingua-plus-plus/Icalingua-plus-plus"
provides=('electron-qq' 'icalingua')
conflicts=('electron-qq')
replaces=('electron-qq' "icalingua-plus-plus")
source=(${_pkgname}.desktop
        ${_pkgname})
source_x86_64=("app-x86_64-${pkgver}.asar::${url}/releases/download/v${pkgver//_/-}/app-x86_64.asar")
source_aarch64=("app-aarch64-${pkgver}.asar::${url}/releases/download/v${pkgver//_/-}/app-arm64.asar")
prepare(){
    cd ${srcdir}
    asar ef app-${CARCH}-${pkgver}.asar dist/electron/static/icons/512x512.png
}
package() {
    install -Dm644 -t "${pkgdir}/usr/share/applications" "${_pkgname}.desktop"
    install -Dm644 "512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$_pkgname.png"
    install -Dm644 "app-${CARCH}-${pkgver}.asar" "${pkgdir}/usr/lib/${_pkgname}/${_pkgname}.asar"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    ln -s "/usr/bin/${_pkgname}" "${pkgdir}/usr/bin/electron-qq"
}
sha256sums=('43da1c99b7a6aee974c20da3bcf925b660dff4ba44a447c86066c84c8bc95fbd'
            '33a02b61af9cd48abd332b6a13964c939649c7ec089bc1a1aca4014bbb8785d2')
sha256sums_aarch64=('1be27a79c3a71620192fb91ca5bacd1d51db5bdb197b24a85d19d49d23751c03')
sha256sums_x86_64=('0a358d64ec1b9f2aa43998523d2d0c372f2121b1f53a777d7d435bb46cb2977d')
