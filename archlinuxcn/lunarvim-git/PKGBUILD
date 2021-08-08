# Maintainer:  edward-p <edward AT edward-p DOT xyz>

pkgname=lunarvim-git
pkgver=0.5.1.r106.g3da49e4b
pkgrel=1
pkgdesc="An IDE layer for Neovim with sane defaults. Completely free and community driven."
arch=('any')
url='https://github.com/LunarVim/LunarVim'
license=('GPL3')
depends=(
  'neovim'
  'lua'
  'git'
  'ripgrep'
  'fzf'
  'neovim-remote'
  'neovim-plenary-git'
  'tree-sitter'
  'python-pynvim'
  'nodejs'
  'yarn')
makedepends=('git')
install=${pkgname}.install
source=("${pkgname}::git+https://github.com/LunarVim/LunarVim.git#branch=rolling"
	"git+https://github.com/nvim-treesitter/nvim-treesitter.git#branch=0.5-compat"
        "init-lvim.sh"
        "lvim")
sha256sums=('SKIP'
            'SKIP'
            '481874f766e0eee893569f327a16c2decb0bc1cbd3536d985aa2964e494db562'
            'cfaa30e851dad37d89c131db0b76d3b2f74961933c109e462c710aab8e78defa')

pkgver() {
  cd "${pkgname}"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build(){
  cd "${srcdir}/nvim-treesitter"
  runtime="${srcdir}/nvim-treesitter"
  count_maintained=$(nvim --cmd "set runtimepath+=${runtime}" --headless \
    +"lua print(#require('nvim-treesitter.parsers').maintained_parsers())" +qall 2>&1)

  while [ "$(ls ${runtime}/parser/ | wc -l)" -lt "${count_maintained}" ]; do
    nvim --cmd "set runtimepath+=${runtime}" --headless \
      +'TSUpdateSync maintained' +qall
  done
}

package() {
  cd "${srcdir}/${pkgname}"

  mkdir -p "${pkgdir}/usr/share/lunarvim"
  cp -r {colors,ftdetect,ftplugin,lua,init.lua} "${pkgdir}/usr/share/lunarvim"
  
  mkdir -p "${pkgdir}/usr/share/lunarvim/prebuild/nvim-treesitter/parser"{,-info}

  for parser in "${srcdir}/nvim-treesitter/parser/"*.so; do
    install -Dm 755 "${parser}" "${pkgdir}/usr/share/lunarvim/prebuild/nvim-treesitter/parser/${parser##/*/}"
  done
  
  for info in "${srcdir}/nvim-treesitter/parser/"*; do
    install -Dm 755 "${info}" "${pkgdir}/usr/share/lunarvim/prebuild/nvim-treesitter/parser/${info##/*/}"
  done

  install -Dm 644 "README.md" "${pkgdir}/usr/share/doc/lunarvim/README.md"
  install -Dm 644 "CONTRIBUTING.md" "${pkgdir}/usr/share/doc/lunarvim/CONTRIBUTING.md"
  install -Dm 644 "utils/installer/config.example.lua" "${pkgdir}/usr/share/doc/lunarvim/config.example.lua"
  install -Dm 644 "utils/installer/config.example-no-ts.lua" "${pkgdir}/usr/share/doc/lunarvim/config.example-no-ts.lua"
  install -Dm 755 "${srcdir}/lvim" "${pkgdir}/usr/bin/lvim"
  install -Dm 755 "${srcdir}/init-lvim.sh" "${pkgdir}/usr/share/lunarvim/init-lvim.sh"
}
