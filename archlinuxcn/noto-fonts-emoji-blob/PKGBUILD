# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
_pkgver=2019-06-14
pkgver=${_pkgver//-}
pkgrel=1
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=("Apache")
depends=(fontconfig)
provides=(noto-fonts-emoji)
source=("https://github.com/C1710/blobmoji/releases/download/v2019-06-14-Emoji-12/Blobmoji.ttf")
sha256sums=('702d0521c6f58476abc9f16f09b6a2943850b1b54cf098f573f6ee4a5ff5db6a')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji.ttf "$pkgdir"/usr/share/fonts/blobmoji
}
