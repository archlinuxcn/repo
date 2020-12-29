# Maintainer: Arne Beer <privat@arne.beer>

pkgname=pueue
pkgver='0.10.0'
pkgrel=1
arch=('any')
pkgdesc='A command scheduler for shells'
license=('MIT')
makedepends=('cargo')
url='https://github.com/nukesor/pueue'
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/Nukesor/pueue/archive/v${pkgver}.tar.gz"
)
md5sums=('07ca78f39dd9dcc1805d522affed8e4d')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    cargo build --release --locked

    ./build_completions.sh
}

package() {
    cd "$srcdir/$pkgname-$pkgver"

    # Install binaries
    install -Dm755 "target/release/pueue" "$pkgdir/usr/bin/pueue"
    install -Dm755 "target/release/pueued" "$pkgdir/usr/bin/pueued"

    # Place systemd user service
    install -Dm644 "utils/pueued.service" "$pkgdir/usr/lib/systemd/user/pueued.service"

    # Install shell completions file
    install -Dm644 "utils/completions/_pueue" "$pkgdir/usr/share/zsh/site-functions/_pueue"
    install -Dm644 "utils/completions/pueue.bash" "$pkgdir/usr/share/bash-completion/completions/pueue.bash"
    install -Dm644 "utils/completions/pueue.fish" "$pkgdir/usr/share/fish/completions/pueue.fish"

    # Install License
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/pueue/LICENSE"
}
