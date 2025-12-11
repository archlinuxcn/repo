# Maintainer: Kimiblock Moe
pkgname=portable-git
epoch=1
pkgver=11.2.r0.gbaced13b
pkgrel=1
epoch=
pkgdesc="Portable Sandboxing framework"
arch=('any')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
provides=(portable)
groups=()
options=(!debug !strip)
conflicts=(portable)

makedepends+=(git)

depends=(
	"libnotify"
	pipewire
	findutils
	"procps-ng"
	"coreutils"
	"xdg-user-dirs"
	"xorg-xhost"
	"zenity"
	"xdg-dbus-proxy"
	"bubblewrap"
	"util-linux"
	"glib2"
	"wayland"
	"dbus"
	"bash"
	"xdg-desktop-portal-impl"
	"inotify-tools"
	"grep"
)

optdepends=(
	'at-spi2-core: accessibility'
	'orca: screen reader'
)

makedepends+=(
	"libarchive"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git)

md5sums=('SKIP')

function pkgver() {
	cd "${srcdir}/portable"
	git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

function package() {
	cd portable
	install -vDm755 portable.sh "${pkgdir}/usr/bin/portable"
	install -d "${pkgdir}/usr/lib/"
	cp -r "${srcdir}/portable/lib" "${pkgdir}/usr/lib/portable"
	install -t "${pkgdir}/usr/share/portable" -Dm755 "${srcdir}/portable/share"/*
	install -vDm755 portable-pools "${pkgdir}/usr/bin/portable-pools"
	install -vDm755 portable-packer "${pkgdir}/usr/bin/portable-packer"
	cp -r "${srcdir}/portable/lib/modules-load.d" "${pkgdir}/usr/lib"
}
