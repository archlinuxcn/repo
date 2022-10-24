pkgname=icalingua++
_pkgname=icalingua
pkgver=2.7.6
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
sha256sums_aarch64=('f1da94ce988031d18e642e6d2d8bcc2e30e36aa0381870fbd98c9f516da171f2')
sha256sums_x86_64=('96e84b2138430ec2c6e891b5a1dd3c085820c796fcc487b87dd665969f3d30cf')
sha256sums_i686=('468a0b8d6b4fd967480e6aa0dc6317847993aa2c4c7f94c3733bd9175d3c62b2')
