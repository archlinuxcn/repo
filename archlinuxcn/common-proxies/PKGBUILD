# Maintainer: Kimiblock Moe

pkgname=common-proxies
arch=('x86_64')
pkgver=3.0.0
pkgrel=2
pkgdesc="Gateways and Rewrite Proxies for UnifiedPush written in Go"
url=https://codeberg.org/UnifiedPush/common-proxies.git
license=("MIT")
depends=("glibc")
source=("git+https://codeberg.org/UnifiedPush/common-proxies.git#tag=v${pkgver}")
makedepends=("go" "git" )
sha256sums=('b8b7872d638fa3a3125c4f0d35c914dad5c17fc6795a1fedf8d452f16940bab1')
provides=("common-proxies")

function prepare(){
	cd "${srcdir}/${pkgname}"
	git submodule init
	git submodule update --depth=1
	export GOPATH="${srcdir}"
	go mod download -modcacherw
}

function build(){
	cd "${srcdir}/${pkgname}"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	go build \
		-trimpath \
		-buildmode=pie \
		-mod=readonly \
		-modcacherw \
		-o output-binary \
		-ldflags "-linkmode external -extldflags \"${LDFLAGS}\"" \
		.
}

function package(){
	cd "${srcdir}/${pkgname}"
	install -Dm755 \
		"${srcdir}/${pkgname}/output-binary" \
		"${pkgdir}/usr/bin/${pkgname}"
	install -Dm644 \
		"${srcdir}/${pkgname}/LICENSE" \
		-t "${pkgdir}/usr/share/licenses/${pkgname}"
}
