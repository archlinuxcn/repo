# Maintainer: Kimiblock Moe

pkgname=stashpak
pkgver=0.6.0
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
sha256sums=('22a300bf0dc30bb0290c5589aea48f1c1ff590f393f40be4137dec176eb8f395')

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
