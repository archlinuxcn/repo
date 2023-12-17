# Maintainer: elomatreb <ole@bertr.am>
pkgname=listenbrainz-mpd
pkgver=2.3.2
pkgrel=2
pkgdesc="ListenBrainz submission client for MPD"
arch=('x86_64')
url='https://codeberg.org/elomatreb/listenbrainz-mpd'
license=('AGPL3')
depends=('sqlite' 'libssl.so=3-64' 'libcrypto.so=3-64')
makedepends=('openssl' 'cargo' 'asciidoctor')
source=("$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate")
sha256sums=('903593c671292be0fb2aaf3e490b265b5fa06815973b67a49af9b8a7808130e1')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    cargo fetch --locked --target "$(rustc -vV | sed -n 's|host: ||p')"
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    export RUSTFLAGS="-C target-cpu=native"
    cargo build --frozen --release --features shell_completion,systemd
    asciidoctor --backend=manpage listenbrainz-mpd.adoc
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm0755 "$srcdir/$pkgname-$pkgver/target/release/listenbrainz-mpd" "$pkgdir/usr/bin/listenbrainz-mpd"
    install -Dm0644 listenbrainz-mpd.service "$pkgdir/usr/lib/systemd/user/listenbrainz-mpd.service"
    install -Dm0644 listenbrainz-mpd.1 "$pkgdir/usr/share/man/man1/listenbrainz-mpd.1"
    install -Dm0644 generated_completions/listenbrainz-mpd.bash "$pkgdir/usr/share/bash-completion/completions/listenbrainz-mpd"
    install -Dm0644 generated_completions/listenbrainz-mpd.fish "$pkgdir/usr/share/fish/vendor_completions.d/listenbrainz-mpd.fish"
    install -Dm0644 generated_completions/_listenbrainz-mpd "$pkgdir/usr/share/zsh/site-functions/_listenbrainz-mpd"
}
