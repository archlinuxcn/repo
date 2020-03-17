# Maintainer: Jay Ta'ala <jay@jaytaala.com>
# Contributor: Claudio d'Angelis <claudiodangelis at gmail dot com>
pkgname=postman-bin
pkgver=7.20.1
pkgrel=1
pkgdesc="Build, test, and document your APIs faster"
arch=('x86_64')
url="https://www.getpostman.com"
license=('custom')
source=(
	"Postman-linux-x64-${pkgver}.tar.gz::https://dl.pstmn.io/download/version/${pkgver}/linux64"
    "postman.desktop"
)
depends=(libxss nss gtk3)
sha256sums=('2a43d511987d84de3cc25e3f966b59e61343ecefe0e4adb5231ab36f7f8d4a56'
            '74b2d8570658e207e31f729e7f4768952252383aee7c695218d077bd0ef13245')
package() {
	install -dm755 "${pkgdir}/opt/"
	chmod -R 755 "Postman"
	cp -r "Postman" "${pkgdir}/opt/postman"
	chmod -R 755 "${pkgdir}/opt/postman"
  	install -dm755 "${pkgdir}/usr/bin"
    ln -s "/opt/postman/Postman" "${pkgdir}/usr/bin/postman"
    # License
    install -D -m644 "Postman/app/LICENSE" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    # Chromium License
    install -D -m644 "Postman/app/LICENSES.chromium.html" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSES.chromium.html"
    # Desktop file
    install -D -m644 "postman.desktop" \
        "${pkgdir}/usr/share/applications/postman.desktop"
    # Icon
    install -d -m755 "${pkgdir}/usr/share/icons/hicolor/128x128/apps"
    ln -s "/opt/postman/app/resources/app/assets/icon.png" \
        "${pkgdir}/usr/share/icons/hicolor/128x128/apps/postman.png"
}
