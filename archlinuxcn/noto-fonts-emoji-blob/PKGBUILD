# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
epoch=1
pkgver=14.0
pkgrel=3
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=(Apache)
provides=(noto-fonts-emoji emoji-font)
source=("Blobmoji-${pkgver}-${pkgrel}.ttf::https://github.com/C1710/blobmoji/releases/download/v${pkgver}/Blobmoji.ttf")
sha256sums=('08826af507f385b33f3db32b31274d86cbf43009ded3433daaecb53154b64620')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji-${pkgver}-${pkgrel}.ttf "$pkgdir"/usr/share/fonts/blobmoji/Blobmoji.ttf
}
