# Maintainer: Kimiblock Moe

pkgname=typesetter
pkgdesc="A minimalist, local-first Typst editor."
url="https://codeberg.org/haydn/typesetter"
license=("GPL-3.0-or-later")
arch=("x86_64")
pkgver=0.5.1
pkgrel=1
makedepends=("rust" "cargo" "git" "blueprint-compiler" "meson" "libvirt" "libvirt-glib" "blueprint-compiler")
depends=(libadwaita gtk4 hicolor-icon-theme dconf gcc-libs glib2 glibc gtksourceview5 libspelling pango gdk-pixbuf2 openssl cairo)
source=("source::git+https://codeberg.org/haydn/typesetter.git#tag=v${pkgver}")
sha256sums=('d1908bf0fd8453a9e7b9a6eccf7dd49b27616e6cbd185e176d17bc1a6d30dadb')
options=()

function prepare() {
	export RUSTUP_TOOLCHAIN=stable
	export RUSTFLAGS="${RUSTFLAGS} --remap-path-prefix $srcdir=src"
	rm -rf build
	cd source
	git clean -fdx
	cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

function build() {
	export RUSTUP_TOOLCHAIN=stable
	export RUSTFLAGS="${RUSTFLAGS} --remap-path-prefix $srcdir=src"
	#export RUST_BACKTRACE=1
	arch-meson "${srcdir}/source" build --buildtype=release
	meson compile -C build
}

function check() {
	export RUSTUP_TOOLCHAIN=stable
	export RUSTFLAGS="${RUSTFLAGS} --remap-path-prefix $srcdir=src"
	meson test -C build --no-rebuild --print-errorlogs

}

function package() {
	meson install \
		-C build \
		--no-rebuild \
		--destdir "${pkgdir}"
}
