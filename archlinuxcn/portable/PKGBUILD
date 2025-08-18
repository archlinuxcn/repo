# Maintainer: Kimiblock Moe
pkgname=portable
epoch=1
pkgver=7.5.2
pkgrel=1
epoch=
pkgdesc="Portable Sandboxing framework"
arch=('any')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
provides=(portable)
groups=()
options=(!debug !strip)

makedepends+=(git)

depends=(
	"libnotify"
	"procps-ng"
	"coreutils"
	"awk"
	"xxd"
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
	"lsb-release"
	"psmisc"
	"flatpak-xdg-utils"
	"xdg-desktop-portal"
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

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('ae040c360a368d43f39f5c6a57151f88')


function package() {
	cd portable
	install -Dm755 portable.sh "${pkgdir}/usr/bin/portable"
	install -d "${pkgdir}/usr/lib/"
	cp -r "${srcdir}/portable/lib" "${pkgdir}/usr/lib/portable"
	install -t "${pkgdir}/usr/share/portable" -Dm755 "${srcdir}/portable/share"/*
	install -Dm755 portable-pools "${pkgdir}/usr/bin/portable-pools"
}
