# Maintainer: Yuuta Liang <yuuta@yuuta.moe>
pkgname=rait
pkgver=4.3.0
pkgrel=1
epoch=
pkgdesc="Redundant Array of Inexpensive Tunnels"
arch=(x86_64)
url="https://gitlab.com/NickCao/RAIT"
license=('custom')
groups=()
depends=(glibc)
makedepends=(go)
checkdepends=()
optdepends=("babeld: Dynamic routing daemon")
provides=()
conflicts=()
replaces=()
backup=(etc/rait/rait.conf)
options=()
install=
changelog=
source=("https://gitlab.com/NickCao/RAIT/-/archive/v$pkgver/RAIT-v$pkgver.tar.gz"
"rait.service"
"rait-metrics.service"
"rait.conf")
noextract=()
sha256sums=('c5c45746ccd0fc4077980dd3bff36efb35003eb91935698e91d81ecf53865e6f'
            '7dce9ea0fbbea74320ae8ab55f92b59630b440e4a516beca03389114417d6d6f'
            'db6854d47284aa1e902edbc01911d48311de82bef3d81fd1f0ca3f67dbea0cb4'
            '7f85c1f0f3979bce2072974b423964aeeb95f05176e0c06bf264b55ff51e53c3')
validpgpkeys=()

prepare() {
	cd "RAIT-v$pkgver"
}

build() {
	cd "RAIT-v$pkgver"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	go build -o build ./cmd/...
}

check() {
	cd "RAIT-v$pkgver"
	go test ./...
}

package() {
	cd "RAIT-v$pkgver"
	install -Dm755 build "$pkgdir"/usr/bin/$pkgname
	mkdir -p "$pkgdir"/usr/share/licenses/$pkgname/
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/license
	cd ..
	mkdir -p "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait.service "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait-metrics.service "$pkgdir"/usr/lib/systemd/system/
	mkdir -p "$pkgdir"/etc/rait/
	install -Dm600 rait.conf "$pkgdir"/etc/rait/
}
