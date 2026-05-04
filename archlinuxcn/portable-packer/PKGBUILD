# Maintainer: Kimiblock Moe

pkgname=portable-packer
pkgver=0.2.1
pkgrel=1
pkgdesc="Packaging utility for Portable"
arch=("x86_64")
url="https://github.com/Kimiblock/stashpak"
license=("GPL-3.0-or-later")
depends=("glibc" coreutils desktop-file-utils git)

makedepends=('go' 'git')
backup=()
source=("source::git+https://github.com/Kimiblock/portable-packer.git#tag=${pkgver}")
sha256sums=('37bbc6ed66659555ae55dfff8154a507a78851e9c98cb534bfa80cca5f92fcc7')

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
