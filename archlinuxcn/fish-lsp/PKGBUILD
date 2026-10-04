# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: tippfehlr <tippfehlr@tippfehlr.eu>
# Contributor: Chewing_Bever
pkgname=fish-lsp
pkgver=1.1.5
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
sha256sums=('b6bbe28d497b22abaad7a3ffe4e315a728bfd1a80c6c2d9ccbf444d2d1884529'
            '78c17e827f9c049267cb37860cb879636a0a5fc5ce57cf828d835d2b4f53cd1b'
            'f2af9d34fc4b90bce7d565513cc7501e718ea683711913a547fb01ecb6e98490')

package() {
    install -Dm755 ${pkgname}-${pkgver} "$pkgdir/usr/bin/fish-lsp"
    install -Dm644 ${pkgname}-${pkgver}-LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 ${pkgname}-${pkgver}-fish-lsp.1 "$pkgdir/usr/share/man/man1/fish-lsp.1"
}
