# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=vim-ripgrep-git
pkgver=r27.ec87af6
pkgrel=2
pkgdesc="Use RipGrep in Vim and display results in a quickfix list."
arch=('any')
url="https://github.com/jremmen/vim-ripgrep"
license=('MIT')
depends=('ripgrep' 'vim')
makedepends=('git')
source=("$pkgname::git+$url.git"
        "https://raw.githubusercontent.com/jremmen/vim-ripgrep/master/LICENSE")
sha256sums=('SKIP'
            '19a409f836b4ae64da5570915a841ff77a6092aa2cd3a06ec3ef8e49ee4eca0d')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    # License
	  install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    # Plugin
    cd $srcdir/$pkgname/plugin
    install -dm755 $pkgdir/usr/share/vim/vimfiles/plugin
    install -Dm644 vim-ripgrep.vim ${pkgdir}/usr/share/vim/vimfiles/plugin/vim-ripgrep.vim
}
# vim set: ts=4 sw=4 et
