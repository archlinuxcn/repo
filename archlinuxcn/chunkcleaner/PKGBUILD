# Maintainer: Kimiblock Moe

pkgname=chunkcleaner
pkgver=0.0.12
pkgrel=1
pkgdesc="Minecraft tool to automatically delete unused chunks/region based on the time played in them."
arch=("any")
url="https://github.com/zeroBzeroT/ChunkCleaner"
license=("MIT")
depends=("glibc")
makedepends=("go" "git")
backup=()
provides=("chunkcleaner")
source=("git+https://github.com/zeroBzeroT/ChunkCleaner.git#tag=${pkgver}")
sha256sums=('0e253b0f209058a1bc5a82daf0c675b55845156dbf4b53a4c8272e9345213cbc')

function pkgver() {
	cd "${srcdir}/ChunkCleaner"
	git describe --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

function prepare() {
	cd "${srcdir}/ChunkCleaner"
}

function build() {
	cd "${srcdir}/ChunkCleaner"
	go build -trimpath -buildmode=pie -mod=readonly -modcacherw -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""
}

function check() {
	cd "${srcdir}/ChunkCleaner"
	go test ./...
}

function package() {
	install -Dm755 "${srcdir}/ChunkCleaner/chunkCleaner" "${pkgdir}/usr/bin/chunkcleaner"
}
