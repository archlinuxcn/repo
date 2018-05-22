# Maintainer: Claudio d'Angelis <claudiodangelis at gmail dot com>
pkgname=postman-bin
pkgver=6.1.2
pkgrel=2
pkgdesc="Build, test, and document your APIs faster"
arch=('x86_64')
url="https://www.getpostman.com"
license=('custom')
source=(
	"Postman-linux-x64-${pkgver}.tar.gz::https://dl.pstmn.io/download/version/${pkgver}/linux64"
    "postman.desktop"
)
md5sums=(
    "0ee78f58d02684b51a20e7c7c12c0285"
    "ebf1903fa3299a8cf3eb578674ee090f"
)
depends=(gconf libxss gtk2 libxtst nss alsa-lib)
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
    ln -s "/opt/postman/resources/app/assets/icon.png" \
        "${pkgdir}/usr/share/icons/hicolor/128x128/apps/postman.png"
}
