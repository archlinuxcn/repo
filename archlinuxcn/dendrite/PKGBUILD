# Maintainer: AlphaJack <alphajack at tuta dot io>
# Maintainer: Stefan Tatschner <stefan@rumpelsepp.org>

pkgname="dendrite"
pkgver=0.9.1
pkgrel=1
pkgdesc="A second-generation Matrix homeserver written in Go"
url="https://matrix-org.github.io/dendrite/"
license=("Apache")
arch=("x86_64" "i686" "armv6h" "armv7h" "aarch64")
makedepends=("go>=1.16")
optdepends=("postgresql: recommended database for large instances")
source=("$pkgname-$pkgver.tar.gz::https://github.com/matrix-org/dendrite/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        "$pkgname.sysusers"
        "$pkgname.tmpfiles"
        "$pkgname.service")
sha256sums=('5a65eb07b47dffefab2e8abe48cd7d37bc59e08c5163b09c63ec1d30cc808d35'
            'aba328d7a7244e82f866f9d0ead0a53e79e1590b9c449ad6d18ff2659cb5e035'
            '8da956f9fcc7c6ea844cea53c823fcfa4376acf04ecd9bceb1a908a85846c90f'
            '2ce2e6fd819087bc47f4b369205afeaf0070dacf3305efcfbec5365bd11af6e7')
install="$pkgname.install"

build(){
 cd "$pkgname-$pkgver"
 export CGO_CPPFLAGS="${CPPFLAGS}"
 export CGO_CFLAGS="${CFLAGS}"
 export CGO_CXXFLAGS="${CXXFLAGS}"
 export CGO_LDFLAGS="${LDFLAGS}"
 export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
 go build "./cmd/dendrite-monolith-server"
 go build "./cmd/generate-config"
 go build "./cmd/generate-keys"
 go build "./cmd/create-account"
}

check(){
 cd "$pkgname-$pkgver"
 export CGO_CPPFLAGS="${CPPFLAGS}"
 export CGO_CFLAGS="${CFLAGS}"
 export CGO_CXXFLAGS="${CXXFLAGS}"
 export CGO_LDFLAGS="${LDFLAGS}"
 export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
 go test "./cmd/dendrite-monolith-server"
}

package(){
 cd "$pkgname-$pkgver"
 install -D -m 755 "$pkgname-monolith-server"      "$pkgdir/usr/bin/$pkgname"
 install -D -m 755 "generate-config"               "$pkgdir/usr/bin/$pkgname-generate-config"
 install -D -m 755 "generate-keys"                 "$pkgdir/usr/bin/$pkgname-generate-keys"
 install -D -m 755 "create-account"                "$pkgdir/usr/bin/$pkgname-create-account"
 install -D -m 644 "$pkgname-sample.monolith.yaml" "$pkgdir/etc/$pkgname/config-example.yaml"
 install -D -m 644 "$srcdir/$pkgname.service"      "$pkgdir/usr/lib/systemd/system/$pkgname.service"
 install -D -m 644 "$srcdir/$pkgname.sysusers"     "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
 install -D -m 644 "$srcdir/$pkgname.tmpfiles"     "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
}
