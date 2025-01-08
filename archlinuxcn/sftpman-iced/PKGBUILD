# Maintainer: Slavi Pantaleev <slavi at devture.com>

pkgname=sftpman-iced
epoch=1
pkgver=2.0.3
pkgrel=0
pkgdesc='A GUI frontend to sftpman (an application for managing and mounting sshfs (SFTP) filesystems)'
url='https://github.com/spantaleev/sftpman-iced-rs'
license=("AGPL-3.0-or-later")
makedepends=('git' 'cargo')
# sftpman-iced requires libsftpman, but pulls it via cargo.
# There's no runtime dependency on sftpman.
depends=('sshfs')
optdepends=('sftpman: CLI version')
replaces=('sftpman-gtk')
arch=('any')
install=$pkgname.install
source=("git+https://github.com/spantaleev/sftpman-iced-rs.git#tag=v$pkgver")
b2sums=('SKIP')

prepare() {
	cd "$srcdir/sftpman-iced-rs"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "$srcdir/sftpman-iced-rs"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release
}

check() {
	cd "$srcdir/sftpman-iced-rs"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$srcdir/sftpman-iced-rs"

	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"

	install -Dm 644 etc/sftpman-iced.desktop $pkgdir/usr/share/applications/$pkgname.desktop
	install -Dm 644 assets/sftpman-iced-512.png $pkgdir/usr/share/pixmaps/$pkgname.png
}
