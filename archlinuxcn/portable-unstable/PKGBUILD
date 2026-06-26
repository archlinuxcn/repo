# Maintainer: Kimiblock Moe
pkgname=portable-unstable
epoch=1
pkgver=17.0.rc.4
pkgrel=1
epoch=1
pkgdesc="Fast, private, efficient sandbox for Linux desktop. Unstable beta versions."
arch=('x86_64' 'aarch64' 'loongarch64')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
provides=(portable)
groups=()
options=()

depends=(
	libseccomp
	"libnotify"
	pipewire
	"coreutils"
	"zenity"
	"xdg-dbus-proxy"
	"bubblewrap"
	"util-linux"
	"glibc"
	"dbus"
	"bash"
	"xdg-desktop-portal-impl"
	"grep"
	"systemd-libs"
	"portable-packer"
)

optdepends=(
	'at-spi2-core: accessibility'
	'orca: screen reader'
	'netsock: Per-app firewall'
	'stashpak: Install Portable packages with ease'
	'bawn: Transient sandbox generator'
)

makedepends+=(
	"libarchive"
	"git"
	"go"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('03e9446d17d73527711cbf718d0b5b78')

function build() {
	cd "${srcdir}/portable"
	export srcdir
	lib/build.sh
}

function package() {
	export srcdir
	export pkgdir
	cd "${srcdir}/portable"
	lib/package.sh

	rm "${pkgdir}/usr/bin/portable-packer" || true
}
