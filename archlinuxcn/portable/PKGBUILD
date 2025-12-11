# Maintainer: Kimiblock Moe
pkgname=portable
epoch=1
pkgver=11.2
pkgrel=1
epoch=1
pkgdesc="Fast, private, efficient sandbox for Linux desktop."
arch=('any')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
provides=(portable)
groups=()
options=(!debug !strip)

makedepends+=(git)

depends=(
	"libnotify"
	"findutils"
	pipewire
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

source=(portable::git+https://github.com/Kraftland/portable.git#tag=${pkgver})

md5sums=('f2a024f6bc3b31dfeb23e93a72c2c2f9')


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
