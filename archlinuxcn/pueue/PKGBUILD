# Maintainer: Arne Beer <privat@arne.beer>

pkgname=pueue
pkgver='0.11.1'
pkgrel=1
arch=('any')
pkgdesc='A command scheduler for shells'
license=('MIT')
makedepends=('cargo')
url='https://github.com/nukesor/pueue'
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/Nukesor/pueue/archive/pueue-v${pkgver}.tar.gz"
)
md5sums=('31e395b42db9d0eeff1d2e750d528c58')

build() {
    ls -ahl
    cd "$srcdir/$pkgname-$pkgname-v$pkgver"
    cargo build --release --locked

    ./build_completions.sh
}

package() {
    cd "$srcdir/$pkgname-$pkgname-v$pkgver"

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
