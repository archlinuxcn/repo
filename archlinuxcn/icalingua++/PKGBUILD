pkgname=icalingua++
_pkgname=icalingua
pkgver=2.9.10
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
sha256sums_aarch64=('7bd5a5544d31f4b808d022dee1be4e3c71aa99a21fc4103aa3738592f3d826ea')
sha256sums_x86_64=('6536328c55f981dacbedcff9243c17a3ed71defab5ba9542e6fafd51e26ba3b0')
