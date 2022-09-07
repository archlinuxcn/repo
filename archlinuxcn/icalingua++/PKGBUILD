pkgname=icalingua++
_pkgname=icalingua
pkgver=2.7.2
pkgrel=1
pkgdesc='A branch of deleted Icalingua,with limited support'
license=('AGPL3')
depends=('ffmpeg' 'electron' 'libappindicator-gtk3')
optdepends=('mongodb-bin: Provides storage'
            'redis: Provides storage')
arch=('aarch64' 'x86_64' 'i686')
url="https://github.com/Icalingua-plus-plus/Icalingua-plus-plus"
provides=('electron-qq' 'icalingua')
conflicts=('electron-qq')
replaces=('electron-qq' "icalingua-plus-plus")
source=(512x512.png
        ${_pkgname}.desktop
        ${_pkgname})
source_x86_64=("app-x86_64-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-x86_64.asar")
source_aarch64=("app-aarch64-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-arm64.asar")
source_i686=("app-i686-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-ia32.asar")

package() {
    install -Dm644 -t "${pkgdir}/usr/share/applications" "${_pkgname}.desktop"
    install -Dm644 "512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$_pkgname.png"
    install -Dm644 "app-${CARCH}-${pkgver}.asar" "${pkgdir}/usr/lib/${_pkgname}/${_pkgname}.asar"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    ln -s "/usr/bin/${_pkgname}" "${pkgdir}/usr/bin/electron-qq"
}
sha256sums=('84c8585e8c18504ed83b0d199831b55b9f8f0eb0a5aa4cb9e3dc01b4a17d0e38'
            '43da1c99b7a6aee974c20da3bcf925b660dff4ba44a447c86066c84c8bc95fbd'
            '71a583dae6d4352481bed0062c82558c627be0dd4917f2179e7d41c46d51d5eb')
sha256sums_aarch64=('0dbf755c8789298c6eac6c96808ad7e17e6a8b2e81b00f53e620281f31558e98')
sha256sums_x86_64=('b6681c512791fd1a14ae4ba8c19fc1c5aa6eab9d2284ac3ff39e44bb5600bf11')
sha256sums_i686=('09f4cb46ff3d0f77e4bc6f2991d9b0269a474f75df1b8e0e623f5cac3f025c8d')
