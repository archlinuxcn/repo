# Maintainer: Kimiblock Moe

pkgname=stashpak
pkgver=0.1
pkgrel=2
pkgdesc="Build Portable packages with ease."
arch=("x86_64")
url="https://github.com/Kimiblock/stashpak"
license=("GPL-3.0-or-later")
depends=("dbus" "glibc" systemd coreutils pacman devtools git)
optdepends=(
	"devtools-cn-git: Arch Linux CN build prefixes"
)
makedepends=('go' 'git')
backup=()
source=("source::git+https://github.com/Kimiblock/stashpak.git#tag=${pkgver}")
sha256sums=('84b1b6b4d04ba1f5f5bea1e21ab18509dacd7c8a4f568360e60d113ca000369d')

function prepare() {
	cd source
}

function build() {
	cd source
	go build -trimpath -buildmode=pie -mod=readonly -modcacherw -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""
}

function check() {
	cd source
	go test ./...
}

function package() {
	install -vDm755 "${srcdir}/source/stashpak" "${pkgdir}/usr/bin/stashpak"
}
