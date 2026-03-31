# Maintainer: Kimiblock Moe
pkgname=portable
epoch=1
pkgver=15.0
pkgrel=1
epoch=1
pkgdesc="Fast, private, efficient sandbox for Linux desktop."
arch=('x86_64' 'aarch64' 'loongarch64')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
provides=(portable)
groups=()
options=(!debug)

depends=(
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
)

makedepends+=(
	"libarchive"
	"git"
	"go"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('1669545d8f0128e6a0aa9f5ff7b3e890')

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
