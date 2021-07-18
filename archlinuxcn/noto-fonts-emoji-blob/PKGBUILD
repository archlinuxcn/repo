# Maintainer: <ipha00@gmail.com>

pkgname=noto-fonts-emoji-blob
epoch=1
pkgver=14.0
pkgrel=1
pkgdesc="Google Noto emoji fonts (blob version, C1710's fork)"
arch=(any)
url="https://github.com/C1710/blobmoji/"
license=(Apache)
provides=(noto-fonts-emoji emoji-font)
source=("https://github.com/C1710/blobmoji/releases/download/v${pkgver}/Blobmoji.ttf")
sha256sums=('ab8e432fc80c4ffabd7cd8e58718268c5a758fdcf75e5e024ef9a2c5ad106bd8')

package() {
    mkdir -p "$pkgdir"/usr/share/fonts/blobmoji
    install -m644 Blobmoji.ttf "$pkgdir"/usr/share/fonts/blobmoji
}
