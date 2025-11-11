# Maintainer: Kimiblock Moe

pkgname=typesetter
pkgdesc="A minimalist, local-first Typst editor."
url="https://codeberg.org/haydn/typesetter"
license=("GPL-3.0-or-later")
arch=("x86_64")
pkgver=0.5.0
pkgrel=2
makedepends=("rust" "cargo" "git" "blueprint-compiler" "meson" "libvirt" "libvirt-glib" "blueprint-compiler")
depends=(libadwaita gtk4 hicolor-icon-theme dconf gcc-libs glib2 glibc gtksourceview5 libspelling pango gdk-pixbuf2 openssl cairo)
source=("source::git+https://codeberg.org/haydn/typesetter.git#tag=v${pkgver}")
sha256sums=('8e4e36adc5e6764219c6faad6c714722c5c473a6a07b8ca3fa085ebc82d2d321')
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
