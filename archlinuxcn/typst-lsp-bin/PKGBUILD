# Maintainer: Jake Leahy <jake@lowerCaseLastName.dev>

pkgname=typst-lsp-bin
pkgver=0.6.2
pkgrel=1
pkgdesc="A brand-new language server for Typst"
arch=("x86_64" "armv7h" "aarch64")
url="https://github.com/nvarner/typst-lsp"
license=("MIT")

source_x86_64=("typst-lsp-x86_64-$pkgver::https://github.com/nvarner/typst-lsp/releases/download/v$pkgver/typst-lsp-linux-x64")
source_armv7h=("typst-lsp-armv7h-$pkgver::https://github.com/nvarner/typst-lsp/releases/download/v$pkgver/typst-lsp-linux-armhf")
source_aarch64=("typst-lsp-aarch64-$pkgver::https://github.com/nvarner/typst-lsp/releases/download/v$pkgver/typst-lsp-linux-arm64")

sha256sums_x86_64=('4122daf98c31823f6ee27478d9e61ff583b645daf70e456a4b4028641c79804d')
sha256sums_armv7h=('7bab993a727fccedeb3478e7ab749aafbd3849e1268d2aee4a55db4b5513e84d')
sha256sums_aarch64=('bf3040f1c6a83fec745135e25b51f93c08d6d38f97678cdda2d8fe3617168423')

provides=("typst-lsp")
depends=("glibc" "gcc-libs")

package() {
  cd "$srcdir/"
  install -Dm 755 typst-lsp-$CARCH-$pkgver "${pkgdir}/usr/bin/typst-lsp"
}
