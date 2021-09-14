# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
epoch=1
pkgver=14.0.1
pkgrel=1
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=(Apache)
provides=(noto-fonts-emoji emoji-font)
source=("Blobmoji-${pkgver}-${pkgrel}.ttf::https://github.com/C1710/blobmoji/releases/download/v${pkgver}/Blobmoji.ttf")
sha256sums=('c3db3bb85e84ea7a2674399e281e004dc181ff9038b13c03bf01d3dd8197cfc8')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji-${pkgver}-${pkgrel}.ttf "$pkgdir"/usr/share/fonts/blobmoji/Blobmoji.ttf
}
