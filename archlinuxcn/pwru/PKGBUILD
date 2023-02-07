# Maintainer: Y7n05h < echo WTduMDVoQHk3bjA1aC5kZXY= | base64 -d >
pkgname=pwru
pkgver=0.0.8
pkgrel=1
pkgdesc="Packet, where are you? -- eBPF-based Linux kernel networking debugger"
arch=("x86_64" "aarch64")
url="https://github.com/cilium/pwru"
license=("GPL2")
conflicts=()
depends=("glibc")
makedepends=("clang" "llvm" "go")
optdepends=()
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('4a639465707a284c735399ad3d72cb9215450e093285fcce16e41345d70f530e')
_arch=""
prepare() {
	if [ $CARCH = "x86_64" ]; then
		_arch='amd64'
	elif [ $CARCH = "aarch64" ]; then
		_arch='arm64'
	fi
	cd "$pkgname-$pkgver"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOPATH="${srcdir}"
	export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"
	go generate "main_$_arch.go"
}
build() {
	cd "$pkgname-$pkgver"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOPATH="${srcdir}"
	export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"
	GOOS=linux GOARCH=$_arch go build \
		-ldflags "-compressdwarf=false -linkmode external -X \"github.com/cilium/pwru/internal/pwru.Version=${pkgver}\"" \
		-o ${pkgname}
}

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 ${pkgname} -t "$pkgdir/usr/bin"
}
