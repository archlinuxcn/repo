# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=0.9.0
pkgrel=1
pkgdesc='TCP relay & SOCKS5/HTTP proxy tool optimized for poor network environments'
arch=('x86_64')
url="https://github.com/HyNetwork/hysteria"
license=('MIT')
makedepends=('go' 'git')
source=("$_pkgbase"::"git+$url.git#tag=v$pkgver"
        hysteria@.service
        hysteria-server@.service
        sysusers.conf
        )
sha256sums=('SKIP'
            'bfa8685eee317d0c1ba4c6b6696e702f93ea777a89cf7e92c27987f7f012ed2a'
            'eb928868a8c4b6d15dedc9923aaa75ef969b6645893194f7e22a89399f677463'
            'abaab463035e67c1e1728e5378b8f4a50960bf80d5005e02b3b2c9468f06150d')

prepare(){
  mkdir -p "$srcdir/gopath"
  export GOPATH="$srcdir/gopath"
  cd "$srcdir/$_pkgbase"
  mkdir -p build/
}

build() {
  cd "$srcdir/$_pkgbase"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS} -DLWIP_NOASSERT"
  export CGO_CXXFLAGS="${CXXFLAGS} -DLWIP_NOASSERT"
  export CGO_LDFLAGS="${LDFLAGS}"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -X 'main.appVersion=$(git describe --tags)'"
  local _goldflags="$_goldflags -X 'main.appCommit=$(git rev-parse HEAD)'"
  local _goldflags="$_goldflags -X 'main.appDate=$(date "+%F %T")'"
  go build \
    -buildmode=pie -trimpath -mod=readonly -modcacherw \
    -o build/$_pkgbase \
    -ldflags "$_goldflags" \
    ./cmd/...
}

#check() {
#  cd "$srcdir/$_pkgbase"
#  go test ./...
#}

package() {
  # install hysteria
  install -Dm755 "$srcdir/$_pkgbase/build/$_pkgbase" "$pkgdir/usr/bin/$_pkgbase"

  # install sysusers
  install -Dm644 "$srcdir/sysusers.conf" "$pkgdir/usr/lib/sysusers.d/hysteria.conf"

  # install systemd service
  install -Dm644 "$srcdir/hysteria@.service" "$pkgdir/usr/lib/systemd/system/hysteria@.service"
  install -Dm644 "$srcdir/hysteria-server@.service" "$pkgdir/usr/lib/systemd/system/hysteria-server@.service"

  # install config directory
  install -dm755 "$pkgdir/etc/hysteria"
}
