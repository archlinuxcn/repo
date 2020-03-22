# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Ariel AxionL <axionl@aosc.io>
pkgname=skim-git
pkgver=r763.43edc25
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

    # Binaries
    install -Dt "$pkgdir"/usr/bin target/release/sk bin/sk-tmux

    # Man Page
    install -Dm644 -t "$pkgdir"/usr/share/man/man1 man/man1/*

    # Completion and keybindings
    install -Dm644 -t "$pkgdir"/usr/share/skim shell/*.bash shell/*.zsh
    install -Dm644 shell/key-bindings.fish "$pkgdir"/usr/share/fish/functions/skim_key_bindings.fish

    # Vim plugin
    install -Dm644 -t "$pkgdir"/usr/share/vim/vimfiles/plugin plugin/skim.vim

    # License
    install -Dm644 -t "$pkgdir"/usr/share/licenses/skim LICENSE
}
# vim set: ts=4 sw=4 et
