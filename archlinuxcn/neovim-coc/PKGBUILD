# Maintainer: Sainnhe Park <sainnhe@gmail.com>
pkgname=neovim-coc
# Coc.nvim creates tags on release branch but the source code is only available on master branch, so I have to use commit hash to specify the version to use.
_hash='344002147beffd48b9de1adedb2502fd6db4a0bb'
pkgver=0.0.82
pkgrel=1
pkgdesc='Intellisense engine for Vim8 & Neovim, full language server protocol support as VSCode'
arch=('any')
url='https://github.com/neoclide/coc.nvim'
license=('MIT')
depends=('neovim' 'nodejs')
optdepends=('npm: for installing coc extensions'
            'yarn: for installing coc extensions'
            'watchman: for workspace_didChangeWatchedFiles feature')
makedepends=('yarn')
provides=('neovim-coc')
conflicts=('neovim-coc')
source=("https://github.com/neoclide/coc.nvim/archive/${_hash}.zip")
sha256sums=('7a3424819e29eb89cc670f7e46f59305abd04c5d93db4ddb17f73890468a89bd')

build() {
    cd "${srcdir}/coc.nvim-${_hash}"
    yarn install --frozen-lockfile --preferred-cache-folder "${srcdir}/.cache"
}

package() {
    cd "${srcdir}/coc.nvim-${_hash}"
    nvim -es --cmd ":helptags doc" --cmd ":q"
    find autoload build data doc package.json plugin -type f -exec \
        install -Dm 644 '{}' "${pkgdir}/usr/share/nvim/runtime/pack/coc/start/coc.nvim/{}" \;
    install -Dm 644 "${srcdir}/coc.nvim-${_hash}/LICENSE.md" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}
