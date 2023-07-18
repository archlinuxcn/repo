# Maintainer: Jay Ta'ala <jay@jaytaala.com>
# Contributor: Claudio d'Angelis <claudiodangelis at gmail dot com>
pkgname=postman-bin
pkgver=10.16.0
pkgrel=1
pkgdesc="Build, test, and document your APIs faster"
provides=('postman')
conflicts=('postman')
arch=('x86_64' 'aarch64')
url="https://www.getpostman.com"
options=(!strip)
license=('custom')
source_x86_64=(
	"postman-${pkgver}-linux-x64.tar.gz::https://dl.pstmn.io/download/version/${pkgver}/linux64"
	"postman.desktop"
)
source_aarch64=(
	"postman-${pkgver}-linux-arm64.tar.gz::https://dl.pstmn.io/download/version/${pkgver}/linux_arm64"
	"postman.desktop"
)
depends=(libxss nss gtk3)
sha256sums_x86_64=('055dff2b282b8f494743dd07896c04b7e76a2f88e87e8f8a4b80192ba70bb47d'
                   'd87542ac18455ff341da7c5efd01db96a01f659b1bf546840aa4ac8bd085802d')
sha256sums_aarch64=('356caa700826e815cad83c25b36323f5483c6be32373c72eb2daae4975b3fc6e'
                    'd87542ac18455ff341da7c5efd01db96a01f659b1bf546840aa4ac8bd085802d')

package() {
	install -dm755 "${pkgdir}/opt/"
	cp -r "Postman" "${pkgdir}/opt/postman"
  	install -dm755 "${pkgdir}/usr/bin"
    ln -s "/opt/postman/Postman" "${pkgdir}/usr/bin/postman"
    # Desktop file
    install -D -m644 "postman.desktop" \
        "${pkgdir}/usr/share/applications/postman.desktop"
    # Icon
    install -d -m755 "${pkgdir}/usr/share/icons/hicolor/128x128/apps"
    ln -s "/opt/postman/app/resources/app/assets/icon.png" \
        "${pkgdir}/usr/share/icons/hicolor/128x128/apps/postman.png"
}
