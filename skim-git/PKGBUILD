# Maintainer: Ariel AxionL <axionl@aosc.io>
pkgname=skim-git
pkgver=r402.0cdf36f
pkgrel=1
pkgdesc="Fuzzy Finder in rust!"
arch=('x86_64')
depends=('bash')
makedepends=('git' 'rust')
optdepends=("vim: Vi Improved, a highly configurable, improved version of the vi text editor."
            "zsh: A very advanced and programmable command interpreter (shell) for UNIX"
            "zsh-completions: Additional completion definitions for Zsh"
            "bash-completion: Programmable completion for the bash shell")
conflicts=("skim")
provides=("skim")
url="https://github.com/lotabout/skim"
license=('MIT')

source=("$pkgname::git+$url"
        "https://raw.githubusercontent.com/lotabout/skim/master/LICENSE")

sha256sums=('SKIP'
            '97b46715104924e7ceb1f9061c21bcc13d61322f306d6b119cd47ccbf86b22ea')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$srcdir/$pkgname/"
    cargo build --release
}

package() {
    # License
    install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    cd $srcdir/$pkgname

    # Vim plugin
    install -Dm644 plugin/skim.vim $pkgdir/usr/share/vim/vimfiles/plugin/skim.vim

    # Completion and keybindings
    install -dm755 $pkgdir/usr/share/skim
    install -m644 shell/*.bash shell/*.zsh $pkgdir/usr/share/skim

    # Binaries
    install -Dm755 bin/sk-tmux $pkgdir/usr/bin/sk-tmux
    install -Dm755 target/release/sk $pkgdir/usr/bin/sk
}
# vim set: ts=4 sw=4 et
