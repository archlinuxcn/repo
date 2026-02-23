# Maintainer: Kimiblock Moe
pkgname=portable-unstable
epoch=1
pkgver=14.0.alpha.6
pkgrel=1
epoch=1
pkgdesc="Fast, private, efficient sandbox for Linux desktop. Unstable beta versions."
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
)

optdepends=(
	'at-spi2-core: accessibility'
	'orca: screen reader'
	'netsock: Per-app firewall'
)

makedepends+=(
	"libarchive"
	"git"
	"go"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('e02da69e904a7cb973de50e5a30534f1')

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
}
