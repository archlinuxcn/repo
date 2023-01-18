# Maintainer: AlphaJack <alphajack at tuta dot io>
# Maintainer: Stefan Tatschner <stefan@rumpelsepp.org>

pkgname="dendrite"
pkgver=0.10.9
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
sha256sums=('f31c66de38d7bd0bfa187c2afc0247f74331777f619db445a7da5f1a58700a3e'
            'aba328d7a7244e82f866f9d0ead0a53e79e1590b9c449ad6d18ff2659cb5e035'
            '620b634419e94cb09423d39ecd7edf859bf458e9d72c35be30610b37acc1e8bf'
            '2ce2e6fd819087bc47f4b369205afeaf0070dacf3305efcfbec5365bd11af6e7')
install="$pkgname.install"

build(){
 cd "$pkgname-$pkgver"
 export CGO_CPPFLAGS="${CPPFLAGS}"
 export CGO_CFLAGS="${CFLAGS}"
 export CGO_CXXFLAGS="${CXXFLAGS}"
 export CGO_LDFLAGS="${LDFLAGS}"
 export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
 install -d -m 755 "bin"
 cd "bin"
 rm -r "../cmd/$pkgname-polylith-multi/"
 for dir in "../cmd/"*/; do
  go build "$dir"
  echo "[OK] built $(basename "$dir")"
 done
}

check(){
 cd "$pkgname-$pkgver"
 export CGO_CPPFLAGS="${CPPFLAGS}"
 export CGO_CFLAGS="${CFLAGS}"
 export CGO_CXXFLAGS="${CXXFLAGS}"
 export CGO_LDFLAGS="${LDFLAGS}"
 export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
 go test "./cmd/$pkgname-monolith-server"
}

package(){
 cd "$pkgname-$pkgver"
 for bin in "bin"/*; do
  if [[ "$bin" =~ .*$pkgname* ]]; then
   install -D -m 755 "$bin" "$pkgdir/usr/bin/$(basename "$bin")"
  else
   install -D -m 755 "$bin" "$pkgdir/usr/bin/$pkgname-$(basename "$bin")"
  fi
 done
 mv "$pkgdir/usr/bin/$pkgname-monolith-server" "$pkgdir/usr/bin/$pkgname"
 install -d -m 750                                 "$pkgdir/etc/$pkgname"
 install -D -m 644 "$pkgname-sample.monolith.yaml" "$pkgdir/etc/$pkgname/config-example.yaml"
 install -D -m 644 "$srcdir/$pkgname.service"      "$pkgdir/usr/lib/systemd/system/$pkgname.service"
 install -D -m 644 "$srcdir/$pkgname.sysusers"     "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
 install -D -m 644 "$srcdir/$pkgname.tmpfiles"     "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
}
