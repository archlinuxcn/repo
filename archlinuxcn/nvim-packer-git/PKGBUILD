# Maintainer: Yufan You <ouuansteve at gmail>

pkgname=nvim-packer-git
pkgver=r370.3715ce4
pkgrel=1
pkgdesc='A use-package inspired plugin manager for Neovim.'
arch=('any')
url='https://github.com/wbthomason/packer.nvim'
_reponame="$(echo "${url}" | rev | cut -d/ -f1 | rev)"
license=('MIT')
depends=('neovim')
makedepends=('git')
source=("git+${url}")
sha256sums=('SKIP')

pkgver() {
    cd "${_reponame}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd "${_reponame}"
    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    find doc lua -type f -exec install -Dm 644 "{}" "${pkgdir}/usr/share/nvim/site/pack/packer/start/packer.nvim/{}" \;
}
