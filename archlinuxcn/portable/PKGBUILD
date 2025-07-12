# Maintainer: Kimiblock Moe
pkgname=portable
epoch=1
pkgver=6.1
pkgrel=2
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

source=(portable-source::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('353b7da3857c05b17ffab9796e0e7b7b')


function package() {
	cd "${srcdir}/portable-source"
	install -Dm755 portable.sh ${pkgdir}/usr/bin/portable
	install -Dm755 open.sh ${pkgdir}/usr/lib/portable/open
	install -Dm755 portable-pools ${pkgdir}/usr/bin/portable-pools
	install -Dm755 flatpak-info ${pkgdir}/usr/lib/portable/flatpak-info
	install -Dm755 bwrapinfo.json ${pkgdir}/usr/lib/portable/bwrapinfo.json
	install -Dm755 portable-helper.sh ${pkgdir}/usr/lib/portable/helper
}
