# Maintainer: Kimiblock Moe

pkgname=portable-packer
pkgver=0.1.6
pkgrel=1
pkgdesc="Packaging utility for Portable"
arch=("x86_64")
url="https://github.com/Kimiblock/stashpak"
license=("GPL-3.0-or-later")
depends=("glibc" coreutils desktop-file-utils git)

makedepends=('go' 'git')
backup=()
source=("source::git+https://github.com/Kimiblock/portable-packer.git#tag=${pkgver}")
sha256sums=('7b9e58b4ec182a5625ecf3afc036eb566f78bce54408ac80c0563e3779691bd6')

conflicts+=("portable<14.99")

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
	install -vDm755 "${srcdir}/source/packer" "${pkgdir}/usr/bin/portable-packer"
}
