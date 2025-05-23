# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: tippfehlr <tippfehlr@tippfehlr.eu>
# Contributor: Chewing_Bever
pkgname=fish-lsp
pkgver=1.0.9_1
_pkgver=${pkgver//_/-}
pkgrel=1
pkgdesc="LSP implementation for the fish shell language"
# tree-sitter contains compiled files
arch=('x86_64')
url="https://github.com/ndonfris/fish-lsp"
license=('MIT')
depends=('fish' 'nodejs' 'python')
makedepends=('git' 'yarn') # 'typescript' tsc doesn’t work
provides=($pkgname)
conflicts=(${pkgname}-git)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('efe3fa30bbc4cf9d17e1f56c44f53361640d5b4531cf4262f1ba3a8fc8dfeadd')

prepare() {
    cd "${pkgname}-${_pkgver}"
    yarn --frozen-lockfile --ignore-scripts
}

build() {
    cd "${pkgname}-${_pkgver}"
    ./node_modules/.bin/tsc
    ./bin/fish-lsp complete >./fish-lsp.fish
}

package() {
    cd "${pkgname}-${_pkgver}"
    mkdir -p "$pkgdir/usr/bin"
    mkdir -p "$pkgdir/usr/lib/node_modules/fish-lsp"

    rm -r node_modules/@types
    cp -r node_modules out package.json fish_files "$pkgdir/usr/lib/node_modules/fish-lsp"
    # nvim-lspconfig doesn’t work without this symlink
    ln -s /usr/lib/node_modules/fish-lsp/node_modules/@esdmr/tree-sitter-fish/tree-sitter-fish.wasm \
        "$pkgdir/usr/lib/node_modules/fish-lsp/"

    printf "%s\n" "#!/usr/bin/env node" "require('/usr/lib/node_modules/fish-lsp/out/cli');" >"$pkgdir/usr/bin/fish-lsp"
    chmod 755 "$pkgdir/usr/bin/fish-lsp"

    install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 "fish-lsp.fish" "$pkgdir/usr/share/fish/vendor_completions.d/fish-lsp.fish"
}
