# Maintainer: Kimiblock Moe

pkgname=portable-packer
pkgver=0.1.5
pkgrel=2
pkgdesc="Packaging utility for Portable"
arch=("x86_64")
url="https://github.com/Kimiblock/stashpak"
license=("GPL-3.0-or-later")
depends=("glibc" coreutils desktop-file-utils git)

makedepends=('go' 'git')
backup=()
source=("source::git+https://github.com/Kimiblock/portable-packer.git#tag=${pkgver}")
sha256sums=('f4b7b4a8e5d5206f42c8ce2e3a266ff66675609151d137936321fdd6790f8f0d')

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
