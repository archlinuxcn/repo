# Maintainer: Kimiblock Moe

pkgname=realitlscanner-git
pkgver=0.2.1.r1.g4dbba8cb
pkgrel=1
pkgdesc="A TLS server scanner for Reality"
arch=("x86_64")
url="https://github.com/XTLS/RealiTLScanner"
license=("MPL-2.0")
depends=("glibc")
makedepends=("go" "git")
backup=()
provides=("realitlscanner")
conflicts=("realitlscanner")
source=("git+${url}.git")
sha256sums=("SKIP")

function pkgver(){
	cd RealiTLScanner
	git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

function build(){
	cd RealiTLScanner
	go build -trimpath -buildmode=pie -mod=readonly -modcacherw -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""
}

function package(){
	cd RealiTLScanner
	install -Dm755 "${srcdir}/RealiTLScanner/RealiTLScanner" "${pkgdir}/usr/bin/realitlscanner"
}
