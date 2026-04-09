# Maintainer: Kimiblock Moe

pkgname=stashpak
pkgver=0.5.0
pkgrel=1
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
sha256sums=('ad064386ed1beea8003eae5206f2ed30b6d81995d27496bce7f7520c3b29e598')

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
