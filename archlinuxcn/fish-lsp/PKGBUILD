# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: tippfehlr <tippfehlr@tippfehlr.eu>
# Contributor: Chewing_Bever
pkgname=fish-lsp
pkgver=1.1.3
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
sha256sums=('c39aca71cb009782e636796011c551541d81e7173e2848964ed28ffbfa2855ee'
            '42d622608175e998ffcdbb53217a6356a578282782a553ef9a86f5192ffcd7c2'
            '554cfed432024784ef0cf26aa149145d0e4757ad5ef1a539d2ae9d06d6518559')

package() {
    install -Dm755 ${pkgname}-${pkgver} "$pkgdir/usr/bin/fish-lsp"
    install -Dm644 ${pkgname}-${pkgver}-LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 ${pkgname}-${pkgver}-fish-lsp.1 "$pkgdir/usr/share/man/man1/fish-lsp.1"
}
