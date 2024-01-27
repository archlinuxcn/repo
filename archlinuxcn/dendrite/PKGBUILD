# Maintainer: AlphaJack <alphajack at tuta dot io>
# Maintainer: Stefan Tatschner <stefan@rumpelsepp.org>

pkgname="dendrite"
pkgver=0.13.6
pkgrel=1
pkgdesc="A second-generation Matrix homeserver written in Go"
url="https://matrix-org.github.io/dendrite/"
license=("Apache")
arch=("x86_64" "i686" "armv6h" "armv7h" "aarch64")
# https://github.com/quic-go/quic-go/wiki/quic-go-and-Go-versions
makedepends=("go")
optdepends=("postgresql: recommended database for large instances")
source=("$pkgname-$pkgver.tar.gz::https://github.com/matrix-org/dendrite/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        "$pkgname.sysusers"
        "$pkgname.tmpfiles"
        "$pkgname.service")
b2sums=('b833a045b22529ce0941612cf49c1e2955c7821d0b42346c4eb542eb0931ba667720f393f8677f4eda468e111d4907d3cc074a69bee7ecff0551454414104b22'
        'bd0cf2ee02603340cb0066a6786896ee5dec048e665516ad4e66913969175876e480470503093dff274377cabf7d9fe5fbe70ded605c9e6d05531a6298a634bc'
        'b35856b8d5a289f5333b0a20658b602da588676cbbc12f543044b014d8b9a244053763bae39acf7ec54387eb738cd518e460996fc687787592c63fd2d7bbd69b'
        '43d6f636b7d8e6d00e0a8f9a5ae7c9ded223d19d22713b7e77314929f76df5d59e58a1ae3685cd8e4123e8300679c2c535207c64d14183894d2fe613dbfce746')
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
