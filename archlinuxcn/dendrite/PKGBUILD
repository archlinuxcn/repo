# Maintainer: AlphaJack <alphajack at tuta dot io>
# Maintainer: Stefan Tatschner <stefan@rumpelsepp.org>

pkgname="dendrite"
pkgver=0.12.0
pkgrel=2
pkgdesc="A second-generation Matrix homeserver written in Go"
url="https://matrix-org.github.io/dendrite/"
license=("Apache")
arch=("x86_64" "i686" "armv6h" "armv7h" "aarch64")
makedepends=("go>=1.18")
optdepends=("postgresql: recommended database for large instances")
source=("$pkgname-$pkgver.tar.gz::https://github.com/matrix-org/dendrite/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        "$pkgname.sysusers"
        "$pkgname.tmpfiles"
        "$pkgname.service")
sha256sums=('858a3650d957431da4e78f82d801eba6eb963fbc4e6d1dd0ecce3d5c244b265d'
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
 go build -v -o "bin/" ./cmd/...
}

check(){
 cd "$pkgname-$pkgver/cmd/$pkgname"
 export CGO_CPPFLAGS="${CPPFLAGS}"
 export CGO_CFLAGS="${CFLAGS}"
 export CGO_CXXFLAGS="${CXXFLAGS}"
 export CGO_LDFLAGS="${LDFLAGS}"
 export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
 go test
}

package(){
 cd "$pkgname-$pkgver"
 # configuration
 install -d -m 750                                 "$pkgdir/etc/$pkgname"
 install -D -m 644 "$pkgname-sample.yaml"          "$pkgdir/etc/$pkgname/config-example.yaml"
 # systemd
 install -D -m 644 "$srcdir/$pkgname.service"      "$pkgdir/usr/lib/systemd/system/$pkgname.service"
 install -D -m 644 "$srcdir/$pkgname.sysusers"     "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
 install -D -m 644 "$srcdir/$pkgname.tmpfiles"     "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
 # if the command does not start with "dendrite-", then rename it
 cd "bin"
 for bin in *; do
  if [[ "$bin" =~ ^$pkgname-* ]]; then
   install -D -m 755 "$bin" "$pkgdir/usr/bin/$bin"
  else
   install -D -m 755 "$bin" "$pkgdir/usr/bin/$pkgname-$bin"
  fi
 done
}
