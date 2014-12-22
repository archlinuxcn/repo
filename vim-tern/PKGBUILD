# Maintainer: Petron <petron@archlinuxcn.org>
pkgname=vim-tern
pkgver=55.c677b66
pkgrel=1
pkgdesc="Tern plugin for Vim"
arch=('any')
url="https://github.com/marijnh/tern_for_vim"
license=('GPL3')
groups=('vim-plugins')
depends=('vim' 'nodejs')
install=vimdoc.install
makedepends=('git')
source=("git+https://github.com/marijnh/tern_for_vim" "vimdoc.install")
sha256sums=('SKIP' 'e74d002d6b3487e337e896cf6b0d8cb6898329df5f3e06aa73ded409baf7d8a7')
_gitname='tern_for_vim'

pkgver() {
    cd $_gitname
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
    cd $srcdir/$_gitname
    npm install
}

package() {
    cd $srcdir/$_gitname
    mkdir -p $pkgdir/usr/share/vim/vimfiles
    rm -f README.md package.json
    cp -r * $pkgdir/usr/share/vim/vimfiles
}
