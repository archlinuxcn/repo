# Maintainer: Kimiblock Moe
pkgname=netsock-git
epoch=1
pkgver=0.2.r0.g1407c03d
pkgrel=1
epoch=
pkgdesc="Per-app firewall for the Portable sandbox"
arch=('x86_64' 'aarch64' 'loongarch64')
url="https://github.com/Kimiblock/netsock"
license=(GPL-3.0-or-later)
provides=(netsock)
groups=()
options=()
conflicts=(netsock)

depends=(
	nftables
	glibc
)

makedepends+=(
	"git"
	"go"
)

checkdepends=()

source=(source::git+https://github.com/Kimiblock/netsock.git)

md5sums=('SKIP')

function pkgver() {
	cd "${srcdir}/source"
	git describe --long --tags --abbrev=8 --always | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

function prepare() {
	cd source
	git clean -fdx
}

function build() {
	cd "${srcdir}/source"
	go mod download -modcacherw
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	go build \
		-trimpath \
		-buildmode=pie \
		-modcacherw \
		-mod=readonly \
		-ldflags "-linkmode external -extldflags \"${LDFLAGS}\"" \
		.
}

function package() {
	cd "${srcdir}/source"
	install -vDm755 top.kimiblock.netsock "${pkgdir}/usr/bin/netsock"
	install -vDm644 netsock.service -t "${pkgdir}/usr/lib/systemd/system"
	install -vDm644 netsock.socket -t "${pkgdir}/usr/lib/systemd/system"
}
