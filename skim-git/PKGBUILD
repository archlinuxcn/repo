# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=skim-git
pkgver=r456.3748433
pkgrel=1
pkgdesc="Fuzzy Finder in rust!"
arch=('x86_64')
depends=('bash')
makedepends=('git' 'rust')
optdepends=("fish: fish keybindings"
            "tmux: fzf-tmux script for launching fzf in a tmux pane"
	        "vim: plugin"
	        "zsh: zsh keybindings")
conflicts=("skim")
provides=("skim")
url="https://github.com/lotabout/skim"
license=('MIT')

source=("$pkgname::git+$url")

sha256sums=('SKIP')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$srcdir/$pkgname/"
    cargo build --release
}

package() {
    cd $srcdir/$pkgname

    # License
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    # Man Page
    install -Dm644 shell/skim.1 $pkgdir/usr/share/man/man1/skim.1

    # Vim plugin
    install -Dm644 plugin/skim.vim $pkgdir/usr/share/vim/vimfiles/plugin/skim.vim

    # Completion and keybindings
    install -dm755 $pkgdir/usr/share/skim
    install -m644 shell/*.bash shell/*.zsh $pkgdir/usr/share/skim

    ## Fish keybindings
	install -Dm644 shell/key-bindings.fish $pkgdir/usr/share/fish/functions/skim_key_bindings.fish

    # Binaries
    install -Dm755 bin/sk-tmux $pkgdir/usr/bin/sk-tmux
    install -Dm755 target/release/sk $pkgdir/usr/bin/sk
}
# vim set: ts=4 sw=4 et
