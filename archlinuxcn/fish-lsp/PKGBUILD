# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: tippfehlr <tippfehlr@tippfehlr.eu>
# Contributor: Chewing_Bever
pkgname=fish-lsp
pkgver=1.1.2
pkgrel=1
pkgdesc="LSP implementation for the fish shell language 🐠"
arch=('x86_64') # tree-sitter contains compiled files
url="https://github.com/ndonfris/fish-lsp"
license=('MIT')
depends=('nodejs')
optdepends=('fish: fish shell')
conflicts=(${pkgname}-git)
source=("${pkgname}-${pkgver}::${url}/releases/download/v${pkgver}/fish-lsp.standalone"
        "${pkgname}-${pkgver}-LICENSE.md"::"https://raw.githubusercontent.com/ndonfris/fish-lsp/refs/tags/v${pkgver}/LICENSE.md"
        "${pkgname}-${pkgver}-fish-lsp.1"::"https://raw.githubusercontent.com/ndonfris/fish-lsp/refs/tags/v${pkgver}/man/fish-lsp.1")
sha256sums=('948cd962a77cac437307e56be5f9b70737207949b623d470c3ffaefeb125f1fd'
            '42d622608175e998ffcdbb53217a6356a578282782a553ef9a86f5192ffcd7c2'
            '3a7343fd1860c6380e5db8813bc1a9da608f48e54cb56cb8f8d6673e11b2f229')

package() {
    install -Dm755 ${pkgname}-${pkgver} "$pkgdir/usr/bin/fish-lsp"
    install -Dm644 ${pkgname}-${pkgver}-LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 ${pkgname}-${pkgver}-fish-lsp.1 "$pkgdir/usr/share/man/man1/fish-lsp.1"
}
