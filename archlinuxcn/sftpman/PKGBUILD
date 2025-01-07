# Maintainer: Slavi Pantaleev <slavi at devture.com>

pkgname=sftpman
epoch=1
pkgver=2.0.0
pkgrel=1
pkgdesc='A CLI application for managing and mounting sshfs (SFTP) filesystems'
url='https://github.com/spantaleev/sftpman-rs'
license=("GPL-3.0-or-later")
makedepends=('git' 'cargo')
depends=('sshfs')
optdepends=('sftpman-iced: GUI frontend for sftpman v2+')
conflicts=('sftpman-python')
replaces=('sftpman-python')
arch=('any')
install=$pkgname.install
source=("git+https://github.com/spantaleev/sftpman-rs.git#tag=v$pkgver")
b2sums=('SKIP')

prepare() {
	cd "$srcdir/sftpman-rs"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "$srcdir/sftpman-rs"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release
}

check() {
	cd "$srcdir/sftpman-rs"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$srcdir/sftpman-rs"

	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"

	install -Dm 644 etc/bash_completion.d/sftpman "$pkgdir/usr/share/bash-completion/completions/sftpman"
	install -Dm 644 etc/fish-completions/sftpman.fish "$pkgdir/usr/share/fish/completions/sftpman.fish"
}
