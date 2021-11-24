pkgname=icalingua
pkgver=2.4.4_Deus_non_vult
pkgrel=1
pkgdesc='A Linux client for QQ and more'
license=('GPL')
depends=('ffmpeg' 'electron13' 'libappindicator-gtk3')
optdepends=('mongodb-bin: Provides storage'
            'redis: Provides storage')
arch=('aarch64' 'x86_64' 'i686')
url="https://github.com/Icalingua/Icalingua"
provides=('electron-qq')
conflicts=('electron-qq')
replaces=('electron-qq')
source=(512x512.png
        ${pkgname}.desktop
        ${pkgname})
source_x86_64=("app-x86_64-${pkgver}.asar::https://github.com/Icalingua/Icalingua/releases/download/v${pkgver//_/-}/app-x86_64.asar")
source_aarch64=("app-aarch64-${pkgver}.asar::https://github.com/Icalingua/Icalingua/releases/download/v${pkgver//_/-}/app-arm64.asar")
source_i686=("app-i686-${pkgver}.asar::https://github.com/Icalingua/Icalingua/releases/download/v${pkgver//_/-}/app-ia32.asar")

package() {
    install -Dm644 -t "${pkgdir}/usr/share/applications" "${pkgname}.desktop"
    install -Dm644 "512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
    install -Dm644 "app-${CARCH}-${pkgver}.asar" "${pkgdir}/usr/share/${pkgname}/${pkgname}.asar"
    install -Dm755 "${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
    ln -s "/usr/bin/${pkgname}" "${pkgdir}/usr/bin/electron-qq"
}
sha256sums=('84c8585e8c18504ed83b0d199831b55b9f8f0eb0a5aa4cb9e3dc01b4a17d0e38'
            '43da1c99b7a6aee974c20da3bcf925b660dff4ba44a447c86066c84c8bc95fbd'
            '139cd2b15c08236aff65ce1d9b2652b9472e3659671b63e522980b0682f22993')
sha256sums_aarch64=('f1f22756eb9867aea935e39359ce854fe5a479fa5ca530833f423f8f45eedc5a')
sha256sums_x86_64=('ad64cddd509fc92d757ffc11af2e2b74387c54e4c8edb72070a14aab182e8381')
sha256sums_i686=('1cbc0e5577014b89f0cdae7dc1de008e82c4dc7d03d8877969e05c9944b18d25')
