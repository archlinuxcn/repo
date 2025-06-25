# Maintainer: Kimiblock Moe

pkgname=snotify
pkgver=0.1.1
pkgrel=2
epoch=1
pkgdesc="Play sounds when receiving a notification."
arch=("any")
url="https://github.com/Kimiblock/snotify"
license=("GPL-2.0-or-later")
depends=("dbus" "glibc" "pipewire" "pipewire-audio" "pipewire-pulse" "wireplumber")
makedepends=('go' 'git')
backup=()
source=("git+https://github.com/Kimiblock/snotify.git#tag=${pkgver}")
sha256sums=('c39c7ce6c8f15598ec6db39239e97ca4e37c721742b182ca4bff3046ca87b701')

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
