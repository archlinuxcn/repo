# Maintainer: elomatreb <ole@bertr.am>
pkgname=listenbrainz-mpd
pkgver=2.0.1
pkgrel=1
pkgdesc="ListenBrainz submission client for MPD"
arch=('x86_64')
url='https://codeberg.org/elomatreb/listenbrainz-mpd'
license=('AGPL3')
depends=('openssl')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate")
sha256sums=('45a58e1d51a6c2c7f27b2790d9fddf979bbbbefeece7013be86d249cf36c36da')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm0755 "$srcdir/$pkgname-$pkgver/target/release/listenbrainz-mpd" "$pkgdir/usr/bin/listenbrainz-mpd"
    install -Dm0644 listenbrainz-mpd.service "$pkgdir/usr/lib/systemd/user/listenbrainz-mpd.service"
    echo "! When upgrading from v1.x to v2.x, you must recreate your configuration file !"
}
