# Maintainer: Kimiblock Moe

pkgname=snotify
pkgver=1.0
pkgrel=1
epoch=1
pkgdesc="Play sounds when receiving a notification."
arch=("any")
url="https://github.com/Kimiblock/snotify"
license=("GPL-2.0-or-later")
depends=("dbus" "glibc" libpulse coreutils)
optdepends=(
	"glib2: Do not disturb support for GNOME"
)
makedepends=('go' 'git')
backup=()
source=("git+https://github.com/Kimiblock/snotify.git#tag=${pkgver}")
sha256sums=('56aeade5e4897d17f045ace8da807954abf0f95f015249ab604185af74605b81')

function prepare() {
	cd "${srcdir}/snotify"
}

function build() {
	cd "${srcdir}/snotify"
	go build -trimpath -buildmode=pie -mod=readonly -modcacherw -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""
}

function check() {
	cd "${srcdir}/snotify"
	go test ./...
}

function package() {
	install -Dm755 "${srcdir}/snotify/snotify" "${pkgdir}/usr/bin/snotify"
	install -Dm644 "${srcdir}/snotify/snotify.service" "${pkgdir}/usr/lib/systemd/user/snotify.service"
	install -Dm644 "${srcdir}/snotify/message.ogg" "${pkgdir}/opt/snotify/message.ogg"
}
