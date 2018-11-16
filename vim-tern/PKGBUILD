# Maintainer: Petron <petron@archlinuxcn.org>
pkgname=vim-tern
pkgver=94.3cffc28
pkgrel=2
pkgdesc="Tern plugin for Vim"
arch=('any')
url="https://github.com/ternjs/tern_for_vim"
license=('MIT')
depends=('vim' 'nodejs' 'npm')
makedepends=('git')
source=("git+https://github.com/ternjs/tern_for_vim")
sha256sums=('SKIP')
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
