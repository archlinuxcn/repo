# Maintainer: Sainnhe Park <sainnhe@gmail.com>
pkgname=neovim-coc
# Coc.nvim creates tags on release branch but the source code is only available on master branch, so I have to use commit hash to specify the version to use.
_hash='7a50d4d9513362aa21cf42646ceca0cb41cb0dbc'
pkgver=0.0.82
pkgrel=5
pkgdesc='Intellisense engine for Vim8 & Neovim, full language server protocol support as VSCode'
arch=('any')
url='https://github.com/neoclide/coc.nvim'
license=('MIT')
depends=('neovim')
optdepends=('npm: for installing coc extensions'
            'yarn: for installing coc extensions'
            'watchman: for workspace_didChangeWatchedFiles feature')
makedepends=('yarn' 'nodejs-lts-gallium')
provides=('neovim-coc')
conflicts=('neovim-coc')
source=("https://github.com/neoclide/coc.nvim/archive/${_hash}.zip")
sha256sums=('50151f2ccde4b19ff286a7157e5567418b2116581ac9f2e58e8aa7b1a7a058a1')

build() {
    cd "${srcdir}/coc.nvim-${_hash}"
    yarn install --frozen-lockfile --preferred-cache-folder "${srcdir}/.cache"
}

package() {
    # Temp fix. Should be moved to depends() in next release
    depends+=('nodejs')

    cd "${srcdir}/coc.nvim-${_hash}"
    nvim -es --cmd ":helptags doc" --cmd ":q"
    find autoload build data doc package.json plugin -type f -exec \
        install -Dm 644 '{}' "${pkgdir}/usr/share/nvim/runtime/pack/coc/opt/coc.nvim/{}" \;
    install -Dm 644 "${srcdir}/coc.nvim-${_hash}/LICENSE.md" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}
