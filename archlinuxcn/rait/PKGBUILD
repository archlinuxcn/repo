# Maintainer: Yuuta Liang <yuuta@yuuta.moe>
pkgname=rait
pkgver=4.3.1
pkgrel=1
epoch=
pkgdesc="Redundant Array of Inexpensive Tunnels"
arch=(x86_64)
url="https://gitlab.com/NickCao/RAIT"
license=('Apache')
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
"rait@.service"
"rait-metrics.service"
"rait-metrics@.service"
"rait.conf")
noextract=()
sha256sums=('44e88924b080a489fe297b0a313ac0f4f3ef776f7ce234c8f7798accff846517'
            'f43c04d33ca5f747d906bff3f00f40fb616f769106b07c754e42510ccb1b45cc'
            'eab1a48388b66f1ee7c323fdfe5c9098752cf5cb3fe2056d783cc9e6d19fd2de'
            'db6854d47284aa1e902edbc01911d48311de82bef3d81fd1f0ca3f67dbea0cb4'
            '0a793cd28d849ca3048c56c4ad31af69becb40af173789235efed26dc8612536'
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
	cd ..
	mkdir -p "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait.service "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait@.service "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait-metrics.service "$pkgdir"/usr/lib/systemd/system/
	install -Dm644 rait-metrics@.service "$pkgdir"/usr/lib/systemd/system/
	mkdir -p "$pkgdir"/etc/rait/
	install -Dm600 rait.conf "$pkgdir"/etc/rait/
}
