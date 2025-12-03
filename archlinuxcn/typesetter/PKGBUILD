# Maintainer: Kimiblock Moe

pkgname=typesetter
pkgdesc="A minimalist, local-first Typst editor."
url="https://codeberg.org/haydn/typesetter"
license=("GPL-3.0-or-later")
arch=("x86_64")
pkgver=0.6.0
pkgrel=2
makedepends=("rust" "cargo" "git" "blueprint-compiler" "meson" "libvirt" "libvirt-glib" "blueprint-compiler")
depends=(libadwaita gtk4 hicolor-icon-theme dconf gcc-libs glib2 glibc gtksourceview5 libspelling pango gdk-pixbuf2 openssl cairo)
source=("source::git+https://codeberg.org/haydn/typesetter.git#tag=v${pkgver}")
sha256sums=('6a888edafe47803686f23018f3f333cfa212777ae75080f50c021dc82b13e200')
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
