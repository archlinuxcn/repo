# Maintainer: Cody Schafer <dev@codyps.com>

pkgname=grpcurl
pkgver=1.9.1
pkgrel=1
pkgdesc="Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers"
arch=(x86_64)
url="https://github.com/fullstorydev/grpcurl"
license=('MIT')
makedepends=('go')
source=(
	"$pkgname-$pkgver.tar.gz::https://github.com/fullstorydev/grpcurl/archive/v$pkgver.tar.gz"
)
sha384sums=('eefb6ad6e1e797254ee4cd31bdd2775ba4aef464bee9b9ee9d5ea16a2cc0f431c5408b6600b53d5ab1c2376c13ae6695')
# really, `grpcurl-bin` should be conflicting with us instead of the oposite
conflicts=('grpcurl-bin')

prepare() {
	cd "$pkgname-$pkgver"
	mkdir -p build
}

build() {
	cd "$pkgname-$pkgver"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	go build -o build ./cmd/...
}

check() {
	cd "$pkgname-$pkgver"
	go test ./...
}

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 build/grpcurl "${pkgdir}/usr/bin/grpcurl"
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
