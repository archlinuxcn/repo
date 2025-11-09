# Maintainer: Kimiblock Moe

pkgname=field-monitor
pkgdesc="Remote-desktop client designed for the GNOME platform. Access virtual machines and other external screens."
url="https://github.com/theCapypara/field-monitor"
license=("GPL-3.0-or-later")
arch=("x86_64")
pkgver=49.0
pkgrel=1
makedepends=("rust" "cargo" "git" "blueprint-compiler" "meson" "libvirt" "libvirt-glib" "blueprint-compiler" "bubblewrap")
depends=(libadwaita gtk4 hicolor-icon-theme dconf gcc-libs glib2 glibc spice-gtk spice-protocol phodav python-pyparsing libcacard spice freerdp2 vte4 json-c libtirpc gtk-vnc)
source=("git+https://github.com/theCapypara/field-monitor#tag=v${pkgver}")
sha256sums=('ca34af6195a730a47605035b68a1ed4944482ee726151d5e993105712917a027')
options=()

function prepare() {
	export RUSTUP_TOOLCHAIN=stable
	export RUSTFLAGS="${RUSTFLAGS} --remap-path-prefix $srcdir=src"
	cd field-monitor
	cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

function build() {
	export RUSTUP_TOOLCHAIN=stable
	export RUSTFLAGS="${RUSTFLAGS} --remap-path-prefix $srcdir=src"
	#export RUST_BACKTRACE=1
	arch-meson "${srcdir}/field-monitor" build --buildtype=release
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
