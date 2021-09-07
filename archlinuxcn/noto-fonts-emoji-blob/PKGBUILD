# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
epoch=1
pkgver=14.0
pkgrel=4
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=(Apache)
provides=(noto-fonts-emoji emoji-font)
source=("Blobmoji-${pkgver}-${pkgrel}.ttf::https://github.com/C1710/blobmoji/releases/download/v${pkgver}/Blobmoji.ttf")
sha256sums=('d23dfeb500551da8f2b0ccc9bee2913557068602cacc2962657d6bc939699524')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji-${pkgver}-${pkgrel}.ttf "$pkgdir"/usr/share/fonts/blobmoji/Blobmoji.ttf
}
