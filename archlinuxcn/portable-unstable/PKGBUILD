# Maintainer: Kimiblock Moe
pkgname=portable-unstable
epoch=1
pkgver=21.alpha.3
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
	"zenity"
	"xdg-dbus-proxy"
	"bubblewrap"
	"glibc"
	"xdg-desktop-portal-impl"
	libgcc
	"systemd-libs"
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
	"rust"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('fc49810118e4f994242b298e5c7ae862')

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
