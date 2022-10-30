# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
epoch=1
pkgver=15.0
pkgrel=1
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=(Apache)
provides=(noto-fonts-emoji emoji-font)
source=("Blobmoji-${pkgver}-${pkgrel}.ttf::https://github.com/C1710/blobmoji/releases/download/v${pkgver}/Blobmoji.ttf")
sha256sums=('dcc3d6675036ba9b35ef574d2221532770b5bd9886cba23c645ef46947eb78f9')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji-${pkgver}-${pkgrel}.ttf "$pkgdir"/usr/share/fonts/blobmoji/Blobmoji.ttf
}
