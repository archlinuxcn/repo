# Maintainer: Kimiblock Moe
pkgname=portable
epoch=1
pkgver=7.0rc7
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
	"procps-ng"
	"coreutils"
	"awk"
	"xxd"
	"xorg-xauth"
	"xdg-user-dirs"
	"xorg-xhost"
	"zenity"
	"xdg-dbus-proxy"
	"nss"
	"bubblewrap"
	"util-linux"
	"libxcb"
	"nspr"
	"zlib"
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
	'way-secure'
)

makedepends+=(
	"libarchive"
)

checkdepends=()

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('7755dbc4e8574dd5964505e5a3175068')


function package() {
	cd portable
	install -Dm755 portable.sh "${pkgdir}/usr/bin/portable"
	install -d "${pkgdir}/usr/lib/"
	cp -r "${srcdir}/portable/lib" "${pkgdir}/usr/lib/portable"
	install -t "${pkgdir}/usr/share/portable" -Dm755 "${srcdir}/portable/share"/*
	install -Dm755 portable-pools "${pkgdir}/usr/bin/portable-pools"
}
