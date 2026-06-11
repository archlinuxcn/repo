# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: tippfehlr <tippfehlr@tippfehlr.eu>
# Contributor: Chewing_Bever
pkgname=fish-lsp
pkgver=1.1.4
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
sha256sums=('82d7007bda41935dba35cde68f8675fd33d50ecfa9a71f8e878c63808d02e42d'
            '78c17e827f9c049267cb37860cb879636a0a5fc5ce57cf828d835d2b4f53cd1b'
            'c2e130351bd086a16d1cd264e7d5d58543ebce2ab062e56f29c5f5851b1a6afb')

package() {
    install -Dm755 ${pkgname}-${pkgver} "$pkgdir/usr/bin/fish-lsp"
    install -Dm644 ${pkgname}-${pkgver}-LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 ${pkgname}-${pkgver}-fish-lsp.1 "$pkgdir/usr/share/man/man1/fish-lsp.1"
}
